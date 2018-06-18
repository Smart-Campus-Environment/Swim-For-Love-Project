import os
import time
from config import *

def open_url(url):
    os.system('osascript -e \'tell application "Safari" to set the URL of the front document to "{}"\''.format(url))

# Activate Safari, open leaderboard page and fullscreen
os.system('''
osascript -e '
tell application "Safari" to activate
tell application "System Events" to keystroke "t" using command down
tell application "System Events" to keystroke "f" using {command down, control down}'
''')

while True:
    open_url(ROOT_URL)
    userid = input('Swimmer ID: ')
    open_url('{}/swimmer/{}'.format(ROOT_URL, uid))
    time.sleep(PERSONAL_SPAN)
