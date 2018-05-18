import os
import json
from PIL import Image
from config import *

def add_photo():
	while True:
		file_list = [files for files in os.listdir(TEMP_PHOTO_PATH) if files.endswith('.jpg')]
		if len(file_list) == 1:
			photo_name = file_list[0]
			picture=Image.open(TEMP_PHOTO_PATH+photo_name)
			picture.thumbnail((1500,1500))
			picture.save(REGISTER_PATH + uid + '.jpg')
			os.remove(TEMP_PHOTO_PATH+photo_name)
			# os.rename(TEMP_PHOTO_PATH + photo_name, REGISTER_PATH + uid + '.jpg')
			print(name+' Photo Addded')
			break
		elif len(file_list) == 0:
			pass
		elif len(file_list) > 1:
			print('There are more than one file in Temp_File Folder')
			input('Please Press Enter after leaving one picture.')
			pass
while True:
	name = input('Name:')
	uid = input('UID:')
	swimmersData = json.load(REGISTER_FILE_PATH.open(encoding='utf-8'))
	swimmersData[uid] = name
	add_photo()
	json.dump(swimmersData, REGISTER_FILE_PATH.open('w', encoding='utf-8'), indent=4)


"""

from PIL import Image
image = Image.open('/Users/hehuang/Desktop/Pic.jpg')
image.thumbnail((1500,1500))
image.save('/Users/hehuang/Desktop/Pic_Reduced.jpg')

"""
