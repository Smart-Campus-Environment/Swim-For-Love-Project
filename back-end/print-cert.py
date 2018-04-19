import os
import time
from utils import *

wait_time = 1
base_url = 'http://localhost/Swim-For-Love-Project'

def demo():
	while True:
		uid = input('UID:').upper()
		open_url('{}/swimmers/{}/cert/'.format(base_url, uid))
		activate('Safari')
		time.sleep(wait_time)
		os.system('osascript -e \'tell application "System Events" to key code 36\'')
		time.sleep(wait_time)
		activate('Terminal')

def activate(appName):
	os.system('''
	osascript -e '
	tell application "{}"
		activate
	end tell
	'
	'''.format(appName))

if __name__ == '__main__':
	demo()
