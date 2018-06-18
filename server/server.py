import json
from pathlib import Path
import logging
from threading import Thread
import shutil
import os
from flask import Flask, Response, request, send_file, send_from_directory, render_template, abort
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit

logging.basicConfig(filename='access.log', level=logging.DEBUG)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.secret_key = b'swim4love'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
socketio = SocketIO(app)

SERVER_ROOT = 'http://leaderboard.swim4love.com:8080'
LAP_LENGTH = 50
DATA_FILE = Path('swimmers.json')
RECORDING_FILE = Path('recording.json')
AVATAR_DIR = Path('avatars')
TEMPLATES_DIR = Path('templates')
SWIMMER_TEMPLATE_SUBDIR = Path('swimmer')
SWIMMER_CERT_SUBDIR = Path('cert')

AVATAR_DIR.mkdir(exist_ok=True)
if not (TEMPLATES_DIR / SWIMMER_TEMPLATE_SUBDIR).is_dir():
    app.logger.error('Missing swimmer template page')
if DATA_FILE.is_file():
    swimmers_data = json.load(DATA_FILE.open(encoding='utf-8'))
else:
    swimmers_data = {}
    json.dump(swimmers_data, DATA_FILE.open('w', encoding='utf-8'))
    app.logger.info('Created swimmers data file')
if RECORDING_FILE.is_file():
    recording_swimmers = json.load(RECORDING_FILE.open(encoding='utf-8'))
else:
    recording_swimmers = []
    json.dump(recording_swimmers, RECORDING_FILE.open('w', encoding='utf-8'))
    app.logger.info('Created recording swimmers file')

######################## API Server ########################

def resp(resp_data, mimetype='application/json'):
    return Response(json.dumps(resp_data), mimetype=mimetype)

@app.route('/swimmer/info/<userid>')
def get_user_info(userid):
    if userid not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    return resp({'status': 0, 'msg': 'Success', 'result': swimmers_data[userid]})

@app.route('/swimmer/avatar/<userid>')
def get_user_avatar(userid):
    if userid not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    avatar_DIR = AVATAR_DIR / '{}.jpg'.format(userid)
    if not avatar_DIR.is_file():
        # return resp({'status': 3, 'msg': 'Swimmer avatar file not found'})
        return send_file((AVATAR_DIR / 'default.jpg').as_posix(), mimetype='image/jpg')
    return send_file(avatar_DIR.as_posix(), mimetype='image/jpg')

@app.route('/swimmer/start-record/<userid>')
def start_record(userid):
    if userid not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    elif userid in recording_swimmers:
        return resp({'status': 7, 'msg': 'Swimmer already being recorded'})
    recording_swimmers.append(userid)
    json.dump(recording_swimmers, RECORDING_FILE.open('w', encoding='utf-8'))
    return resp({'status': 0, 'msg': 'Success'})

@app.route('/swimmer/stop-record/<userid>')
def stop_record(userid):
    if userid not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    elif userid not in recording_swimmers:
        return resp({'status': 8, 'msg': 'Swimmer is not being recorded'})
    recording_swimmers.remove(userid)
    json.dump(recording_swimmers, RECORDING_FILE.open('w', encoding='utf-8'))
    return resp({'status': 0, 'msg': 'Success'})

@app.route('/swimmer/addlap/<userid>')
def add_lap(userid):
    if userid not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    elif userid not in recording_swimmers:
        return resp({'status': 8, 'msg': 'Swimmer is not being recorded'})
    swimmers_data[userid]['laps'] += 1
    broadcast_swimmers()
    return resp({'status': 0, 'msg': 'Success', 'result': swimmers_data[userid]})

@app.route('/swimmer/sublap/<userid>')
def subtract_lap(userid):
    if userid not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    elif userid not in recording_swimmers:
        return resp({'status': 8, 'msg': 'Swimmer is not being recorded'})
    elif swimmers_data[userid]['laps'] == 0:
        return resp({'status': 9, 'msg': 'Already 0 laps'})
    swimmers_data[userid]['laps'] -= 1
    broadcast_swimmers()
    return resp({'status': 0, 'msg': 'Success', 'result': swimmers_data[userid]})

@app.route('/swimmer/setlap/<userid>/<laps>')
def set_lap(userid, laps):
    if userid not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    elif not laps.isdigit():
        return resp({'status': 2, 'msg': 'Invalid value for `laps` param'})
    elif userid not in recording_swimmers:
        return resp({'status': 8, 'msg': 'Swimmer is not being recorded'})
    swimmers_data[userid]['laps'] = int(laps)
    broadcast_swimmers()
    return resp({'status': 0, 'msg': 'Success', 'result': swimmers_data[userid]})

# @app.route('/swimmer/new', methods=['POST'])
# def new_user():
#     user_id = request.form.get('id')
#     user_name = request.form.get('name')
#     user_laps = request.form.get('laps', '0')
#     user_avatar = request.files.get('avatar')
#     if not all((user_id, user_name, user_avatar)):
#         return resp({'status': 4, 'msg': 'Missing value or file for new swimmer, requires `id`, `name` and `avatar`'})
#     elif not (len(user_id) == 5 and user_id.isdigit()):
#         return resp({'status': 5, 'msg': 'Invalid swimmer ID'})
#     elif user_id in swimmers_data:
#         return resp({'status': 6, 'msg': 'Existing swimmer ID'})
#     elif not user_laps.isdigit():
#         return resp({'status': 2, 'msg': 'Invalid value for `laps` param'})
#     swimmers_data[user_id] = {'id': user_id, 'name': user_name, 'laps': int(user_laps)}
#     user_avatar.save((AVATAR_DIR / '{}.jpg'.format(user_id)).as_posix())
#     broadcast_swimmers()
#     return resp({'status': 0, 'msg': 'Success'})

@app.route('/swimmer/new', methods=['POST'])
def new_user():
    user_id = request.form.get('id')
    user_name = request.form.get('name')
    user_laps = request.form.get('laps', '0')
    user_avatar = request.files.get('avatar')
    if not all((user_id, user_name)):
        return resp({'status': 4, 'msg': 'Missing value or file for new swimmer, requires `id` and `name`'})
    elif not (len(user_id) == 5 and user_id.isdigit()):
        return resp({'status': 5, 'msg': 'Invalid swimmer ID'})
    elif user_id in swimmers_data:
        return resp({'status': 6, 'msg': 'Existing swimmer ID'})
    elif not user_laps.isdigit():
        return resp({'status': 2, 'msg': 'Invalid value for `laps` param'})
    swimmers_data[user_id] = {'id': user_id, 'name': user_name, 'laps': int(user_laps)}
    if user_avatar:
        user_avatar.save((AVATAR_DIR / '{}.jpg'.format(user_id)).as_posix())
    broadcast_swimmers()
    return resp({'status': 0, 'msg': 'Success'})

@app.route('/swimmer/update/avatar', methods=['POST'])
def update_avatar():
    user_id = request.form.get('id')
    user_avatar = request.files.get('avatar')
    if not all((user_id, user_avatar)):
        return resp({'status': 10, 'msg': 'Missing value or file for updating swimmer\'s avatar, requires `id` and `avatar`'})
    elif user_id not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    user_avatar.save((AVATAR_DIR / '{}.jpg'.format(user_id)).as_posix())
    return resp({'status': 0, 'msg': 'Success'})

@app.route('/swimmer/update/name', methods=['POST'])
def update_name():
    user_id = request.form.get('id')
    user_name = request.form.get('name')
    if not all((user_id, user_name)):
        return resp({'status': 11, 'msg': 'Missing value for updating swimmer\'s name, requires `id` and `name`'})
    elif user_id not in swimmers_data:
        return resp({'status': 1, 'msg': 'Swimmer ID not found'})
    swimmers_data[user_id]['name'] = user_name
    broadcast_swimmers()
    return resp({'status': 0, 'msg': 'Success'})

######################## Flask(80) Server ########################

@app.route('/80/swimmer/<userid>/cert/')
@app.route('/80/swimmer/<userid>/cert')
def personal_cert(userid):
    if userid not in swimmers_data:
        return '' # don't abort 404 to save certificate paper
    name = swimmers_data[userid]['name']
    meters = swimmers_data[userid]['laps'] * LAP_LENGTH
    return render_template((SWIMMER_TEMPLATE_SUBDIR / SWIMMER_CERT_SUBDIR / 'index.html').as_posix(), name=name, meters=meters)

@app.route('/80/swimmer/<userid>/', defaults={'path': 'index.html'})
@app.route('/80/swimmer/<userid>', defaults={'path': 'index.html'})
@app.route('/80/swimmer/<userid>/<path:path>')
def personal_page(userid, path):
    if userid not in swimmers_data:
        abort(404)
    if path in ('index.html', 'main.js', 'confetti.js'):
        return render_template((SWIMMER_TEMPLATE_SUBDIR / path).as_posix(), root=SERVER_ROOT, userid=userid)
    return send_from_directory((TEMPLATES_DIR / SWIMMER_TEMPLATE_SUBDIR).as_posix(), path)

######################## SocketIO Server ########################

@socketio.on('connect')
def new_connection():
    app.logger.info('New leaderboard connection')
    emit('init', swimmers_data, json=True)

def broadcast_swimmers():
    socketio.emit('swimmers', swimmers_data, json=True)
    json.dump(swimmers_data, DATA_FILE.open('w', encoding='utf-8'), indent=2)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
    # app.run(host='0.0.0.0', port=8080)
