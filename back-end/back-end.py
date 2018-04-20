'''
   _______          _______ __  __    ______ ____  _____     _      ______      ________
  / ____\ \        / /_   _|  \/  |  |  ____/ __ \|  __ \   | |    / __ \ \    / /  ____|
 | (___  \ \  /\  / /  | | | \  / |  | |__ | |  | | |__) |  | |   | |  | \ \  / /| |__
  \___ \  \ \/  \/ /   | | | |\/| |  |  __|| |  | |  _  /   | |   | |  | |\ \/ / |  __|
  ____) |  \  /\  /   _| |_| |  | |  | |   | |__| | | \ \   | |___| |__| | \  /  | |____
 |_____/    \/  \/   |_____|_|  |_|  |_|    \____/|_|  \_\  |______\____/   \/   |______|   2018

'''

import random
import time
import shutil
import pickle
import json
import sys
import os
import requests
import urllib
from config import *
from utils import *

logger = Logger('main')

DEBUG = False
timestamps = {}

class Swimmer:
	'''Base class for swimmers.'''

	def __init__(self, uid='', name='Anonymous', lapCount=0):
		self.uid = uid.upper()
		self.name = name
		self.lapCount = lapCount
		self.stat = {'name': self.name, 'uid': self.uid, 'laps': self.lapCount}
		self.dir = SWIMMERS_DIR / self.uid
		self.statFile = self.dir / 'stat.json'
		# Create player's directory
		if not self.dir.is_dir():
			shutil.copytree(EXAMPLE_DIR.as_posix(), self.dir.as_posix())
			avatarFile = Path('photos/{}.jpg'.format(self.uid))
			if avatarFile.is_file():
				shutil.copy(avatarFile.as_posix(), (self.dir / 'avatar.jpg').as_posix())

	def add_lap(self, n=1):
		self.lapCount += n
		self.stat['laps'] = self.lapCount

	def update_stat(self):
		'''Update the data in the user's JSON data file.'''
		json.dump(self.stat, self.statFile.open('w', encoding='utf-8'), indent=4)

def dump_data():
	'''Dump swimmers data into pickle file.'''
	with PICKLE_FILE.open('wb') as f:
		pickle.dump(swimmers, f, protocol=pickle.HIGHEST_PROTOCOL)

def load_data():
	'''Load stored data from pickle file.'''
	global swimmers
	if PICKLE_FILE.is_file():
		with PICKLE_FILE.open('rb') as f:
			swimmers = pickle.load(f)
	else:
		swimmers = []
		dump_data()

def gen_rand_data():
	'''Simulate and generate random scanned data.'''
	num_detected = random.randint(0, len(swimmers))
	n = random.randint(0, 5)
	scanned = {}

	while n < len(swimmers):
		scanned[swimmers[n].uid] = -random.randint(5, 100)
		n += random.randint(0, 3)
	if DEBUG:
		logger.debug(json.dumps(scanned, sort_keys=True, indent=4))
	json.dump(scanned, SWIMMER_SCAN_FILE.open('w', encoding='utf-8'), indent=4)

def analyze_data():
	'''Analyze swimmer's data and add laps accordingly.'''
	scanned_data = {}
	req = requests.get(SCANNED_URL)
	if req.status_code == 200:
		scanned_data = req.json()
	else:
		logger.error('Invalid response code getting scanned data: [{}]'.format(req.status_code))
		return -1

	if DEBUG:
		logger.debug(scanned_data)
	for uid, strength in scanned_data.items():
		for swimmer, ticks in timestamps.items():
			timestamp = time.time()
			if swimmer.uid == uid and timestamp - ticks > DETECTION_INTERVAL and MIN_SIGNAL_STRENGTH < strength < MAX_SIGNAL_STRENGTH:
				timestamps[swimmer] = timestamp
				swimmer.add_lap()
				if DEBUG:
					logger.debug('Added lap for {}'.format(swimmer.name))
				break

def delete_data_files():
	'''Deletes all data files, including the pickle file,
	swimmers directories, stat_all.json, scanned.json'''
	confirm = input('This will remove all data files, proceed? [Y/N]: ')
	if confirm.upper() in ('Y', 'YES'):
		for f in (PICKLE_FILE, STAT_FILE, SWIMMER_SCAN_FILE, SWIMMERS_DIR):
			if f.is_file():
				f.unlink()
			elif f.is_dir():
				shutil.rmtree(f.as_posix())
			else:
				logger.warning('Cannot find file or directory \'{}\''.format(f.as_posix()))
		logger.info('Files removed')
	else:
		logger.info('Files not removed')

def add_swimmer():
	'''Manually append a user to swimmers.'''
	uid = input('UID: ')
	for swimmer in swimmers:
		if uid == swimmer.uid:
			logger.info('Swimmer ID exists')
			return
	name = input('Name: ')
	for swimmer in swimmers:
		if name == swimmer.name:
			confirm = input('Swimmer name exists, proceed? [Y/N]: ')
			if confirm.upper() in ('N', 'NO'):
				return
			break
	swimmers.append(Swimmer(uid, name))

def update_stat():
	'''Save data for all swimmers and all data.'''
	allData = {}
	for swimmer in swimmers:
		json.dump(swimmer.stat, swimmer.statFile.open('w', encoding='utf-8'), indent=4)
		allData[swimmer.uid] = [swimmer.name, swimmer.lapCount]
	json.dump(allData, STAT_FILE.open('w', encoding='utf-8'), indent=4)
	dump_data()

def get_registers():
	'''Get register info from a remote server.'''
	global timestamps
	req = requests.get(REGISERS_URL+'register.json')
	if req.status_code == 200:
		regs = req.json()
	else:
		logger.error('Invalid response code getting registers: [{}]'.format(req.status_code))
		return -1
	swimmerIds = [swimmer.uid for swimmer in swimmers]
	for uid, name in regs.items():
		if uid not in swimmerIds:
			swimmers.append(Swimmer(uid, name))
			timestamps = {swimmer: 0 for swimmer in swimmers}
			url=REGISERS_URL+uid+'.jpg'
			try:
				urllib.request.urlretrieve(url,'swimmers/'+uid+'/avatar.jpg')
				if DEBUG:
					logger.debug(name+' Photo Added')
			except:
				logger.debug(name+' Photo Not Found')

def demo():
	'''A demonstration that simulates the real life situation.'''
	while True:
		if DEBUG:
			os.system('clear')
		get_registers()
		gen_rand_data() # remove in non-demo environment
		analyze_data()
		update_stat()
		time.sleep(1)

if __name__ == '__main__':
	swimmers = []
	if '--debug' in sys.argv or '-d' in sys.argv:
		DEBUG = True
	if '--clear-data' in sys.argv or '-c' in sys.argv:
		delete_data_files()
		exit()
	if '--help' in sys.argv or '-h' in sys.argv:
		print(HELP_MSG)
		exit()
	if ('--new' in sys.argv or '-n' in sys.argv) or not PICKLE_FILE.is_file():
		get_registers()
	else:
		load_data()
	timestamps = {swimmer: 0 for swimmer in swimmers}
	try:
		demo()
	except KeyboardInterrupt:
		# dump_data()
		# logger.info('Good bye')
		pass
