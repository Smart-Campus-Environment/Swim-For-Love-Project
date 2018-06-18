import os
import time
from utils import *

wait_time = 5
base_url = 'http://localhost/Swim-For-Love-Project'

def demo():
	os.system('''
	osascript -e '
	tell application "Safari"
		activate
	end tell

	tell application "System Events" to keystroke "t" using command down
	tell application "System Events" to keystroke "f" using {command down, control down}
	'
	''')
	''' Remove click 'Always show toolbar'
	tell application "System Events"
		tell process "Safari"
			tell menu item "Always Show Toolbar in Full Screen" of menu "View" of menu bar 1
				if value of attribute "AXMenuItemMarkChar" is "✓" then click
			end tell
		end tell
	end tell
	'''
	while True:
		open_url(base_url)
		uid = input('UID:').upper()
		open_url('{}/swimmers/{}/'.format(base_url, uid))
		time.sleep(wait_time)

if __name__ == '__main__':
	demo()
