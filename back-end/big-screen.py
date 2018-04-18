import os
import time

wait_time = 5
base_url= 'http://localhost/Swim-For-Love-Project'


def browser(url):
	os.system("""osascript -e 'tell application "Safari" to set the URL of the front document to " """+url+""" "'""")

def Demo():
	while True:
		browser(base_url)
		UID=input('UID:').upper()
		browser(base_url+'/swimmers/'+UID+'/index.html')
		time.sleep(wait_time)



os.system("""
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
	""")


Demo()
