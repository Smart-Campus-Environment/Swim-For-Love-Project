import os
import time

wait_time = 1
base_url= 'http://localhost/Swim-For-Love-Project'

def browser(url):
	os.system("""osascript -e 'tell application "Safari" to set the URL of the front document to " """+url+""" "'""")

def Demo():
	while True:
		UID=input('UID:').upper()
		browser(base_url+'/swimmers/'+UID+'/cert/')
		activate_Safari()
		time.sleep(wait_time)
		os.system("""osascript -e 'tell application "System Events" to key code 36'""")
		time.sleep(wait_time)
		activate_Terminal()





def activate_Safari():
	os.system("""
	osascript -e '
	tell application "Safari"
		activate
	end tell
	'
		""")

def activate_Terminal():
	os.system("""
	osascript -e '
	tell application "Terminal"
		activate
	end tell
	'
		""")


Demo()
