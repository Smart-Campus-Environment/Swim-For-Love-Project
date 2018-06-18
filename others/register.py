import os
from time import sleep
import requests
from PIL import Image
from config import *

def get_avatar(userid):
    filenos = [int(file.strip('.JPG')) for file in os.listdir(LOCAL_AVATAR_DIR) if file.endswith('.JPG')]
    avatar = LOCAL_AVATAR_DIR / '{}.jpg'.format(max(filenos))
    avatar_path = avatar.as_posix() if avatar.is_file() else DEFAULT_AVATAR.as_posix()
    im = Image.open(avatar_path)
    w, h = im.size
    if w != h:
        k = (max(w, h) - min(w, h)) // 2
        if w > h:
            im.crop((k, 0, h + k, h))
        else:
            im.crop((0, k, w, w + k))
    im.thumbnail(AVATAR_SIZE)
    im.save(avatar_path)
    return avatar_path

while True:
    userid = input('\nSwimmer ID: ')
    if requests.get(CHECK_URL.format(userid)).json()['status'] != 0:
        # New swimmer
        name = input('Name: ')
        hasAvatar = input('Press enter after avatar has been taken, enter \'x\' if no avatar: ')
        if not hasAvatar:
            sleep(3)
            avatar = get_avatar(userid)
            ret = requests.post(NEW_SWIMMER_URL, data={'id': userid, 'name': name}, files={'avatar': open(avatar, 'rb')}).json()
        else:
            ret = requests.post(NEW_SWIMMER_URL, data={'id': userid, 'name': name}).json()
        if ret['status'] == 0:
            print('Successfully added swimmer {}'.format(userid))
        else:
            print('[ERROR] {}'.format(ret['msg']))
    else:
        # Existing swimmer
        name = input('New name, press enter to not update name: ')
        hasAvatar = input('Press enter after new avatar has been taken, enter \'x\' if no avatar: ')
        if name:
            ret = requests.post(UPDATE_NAME_URL, data={'id': userid, 'name': name}).json()
            if ret['status'] == 0:
                print('Successfully updated name for swimmer {}'.format(userid))
            else:
                print('[ERROR] {}'.format(ret['msg']))
        if not hasAvatar:
            sleep(3)
            avatar = get_avatar(userid)
            ret = requests.post(UPDATE_AVATAR_URL, data={'id': userid}, files={'avatar': open(avatar, 'rb')}).json()
            if ret['status'] == 0:
                print('Successfully updated avatar for swimmer {}'.format(userid))
            else:
                print('[ERROR] {}'.format(ret['msg']))

