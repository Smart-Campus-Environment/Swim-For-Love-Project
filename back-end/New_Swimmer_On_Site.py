import os
import json
from config import *

def Add_Photo():
	file_list=[]
	for files in os.listdir(TEMP_PHOTO_PATH):
		if files.endswith('.jpg'):
			file_list.append(files)
	if len(file_list) ==1:
		photo_name=file_list[0]
		os.rename(TEMP_PHOTO_PATH+photo_name,REGISTER_PATH+uid+'.jpg')
	elif len(file_list)==0:
		decision=input('Photo does not exist in File, proceed? (Y/N):').lower()
		if decision=='y' or decision=='yes':
			pass
		else:
			input('Please Press Enter after taking photo')
			Add_Photo()
	elif len(file_list)>1:
		print('There are more than one file in Temp_File Folder')
		input('Please Press Enter after leaving one picture.')
		Add_Photo()

name=input('Name:')
uid=input('UID:')
Swimmer_Database = json.load(REGISTER_FILE_PATH.open(encoding='utf-8'))
Swimmer_Database[uid]=name
Add_Photo()
json.dump(Swimmer_Database,Path(REGISTER_FILE_PATH).open('w', encoding='utf-8'), indent=4)

