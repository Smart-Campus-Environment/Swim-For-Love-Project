import os
import time

wait_time = 5

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

def browser(url):
	os.system("""osascript -e 'tell application "Safari" to set the URL of the front document to "http://"""+url+""" "'""")

def Demo():
	while True:
		browser('localhost/Swim-For-Love-Project/')
		UID=input('UID:').upper()
		browser('localhost/Swim-For-Love-Project/swimmers/'+UID+'/index.html')
		time.sleep(wait_time)
