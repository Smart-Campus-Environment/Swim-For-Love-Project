import os
from time import sleep

def activate(app):
    os.system('osascript -e \'tell application "{}" to activate\''.format(app))

while True:
    userid = input('Swimmer ID: ')
    # Open swimmer certificate page
    os.system('''
    osascript -e '
    tell application "Google Chrome"
        if it is running then quit
        activate
        open location "{}/swimmer/{}/cert"
    end tell'
    '''.format(ROOT_URL, userid))
    # Press command p
    os.system('osascript -e \'tell application "System Events" to keystroke "p" using {option down, command down}\'')
    sleep(3)
    # Press enter
    os.system('osascript -e \'tell application "System Events" to key code 36\'')
    sleep(0.5)
    # Focus back to terminal
    os.system('osascript -e \'tell application "Terminal" to activate\'')
