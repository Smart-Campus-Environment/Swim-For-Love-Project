import os
import time
from utils import *


base_url = 'http://localhost/Swim-For-Love-Project'

def demo():
	while True:
		uid = input('UID:').upper()
		# open_url('{}/swimmers/{}/cert/'.format(base_url, uid))
		os.system("""osascript -e'
tell application "Google Chrome"
	if it is running then
		quit
	end if
	activate
	open location " """+base_url+'/swimmers/'+uid+'/cert/'+""" "
end tell'
			""")
		# activate('')
		time.sleep(3)
		os.system('osascript -e \'tell application "System Events" to key code 36\'')
		time.sleep(0.5)
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
