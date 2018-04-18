import os
import time

wait_time = 5
base_url= 'http://localhost/Swim-For-Love-Project'

def open_url(url):
	os.system('osascript -e "tell application \'Safari\' to set the URL of the front document to \'{}\' "'.format(base_url))

def demo():
    os.system('''
    osascript -e '
    tell application "Safari"
    	activate
    end tell

    tell application "System Events" to keystroke "f" using {command down, control down}

    tell application "System Events"
    	tell process "Safari"
    		tell menu item "Always Show Toolbar in Full Screen" of menu "View" of menu bar 1
    			if value of attribute "AXMenuItemMarkChar" is "✓" then click
    		end tell
    	end tell
    end tell
    '
    ''').strip()
	while True:
		open_url(base_url)
		uid = input('UID:').upper()
        open_url('{}/swimmers/{}/'.format(base_url, uid))
		time.sleep(wait_time)

if __name__ == '__main__':
    demo()
