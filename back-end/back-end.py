"""
   _______          _______ __  __   ______ ____  _____    _      ______      ________ 
  / ____\ \        / /_   _|  \/  | |  ____/ __ \|  __ \  | |    / __ \ \    / /  ____|
 | (___  \ \  /\  / /  | | | \  / | | |__ | |  | | |__) | | |   | |  | \ \  / /| |__   
  \___ \  \ \/  \/ /   | | | |\/| | |  __|| |  | |  _  /  | |   | |  | |\ \/ / |  __|  
  ____) |  \  /\  /   _| |_| |  | | | |   | |__| | | \ \  | |___| |__| | \  /  | |____ 
 |_____/    \/  \/   |_____|_|  |_| |_|    \____/|_|  \_\ |______\____/   \/   |______|
                                                                                       
                                                                                       
"""

import random
import time
import shutil
from pathlib import Path
import pickle
import json
import sys
import os


SWIMMERS_DIR = Path('swimmers')
EXAMPLE_DIR = Path('resources/swimmer_template')
PICKLE_FILE = Path('Swimmer_Database.pickle')
STAT_FILE = Path('stat_all.json')
SWIMMER_SCAN_FILE = Path('scanned.json')
MINIMUM_SIGNAL_STRENGTH = -50
MAXIMUM_SIGNAL_STRENGTH = -5
TIME_INTERVAL_BETWEEN_DETECTION = 20
class Swimmer:
	'''Base class for all swimmers.'''

	def __init__(self, uid='', name='John Doe', lapCount=0):
		self.uid = uid
		self.name = name
		self.lapCount = lapCount
		self.stat = {'name': self.name, 'uid': self.uid, 'laps': self.lapCount}
		self.dir = SWIMMERS_DIR / self.uid
		self.statFile = self.dir / 'stat.json'
		# Create player's directory
		if not self.dir.is_dir():
			# self.dir.mkdir(parents=True, exist_ok=True)
			shutil.copytree(EXAMPLE_DIR.as_posix(), self.dir.as_posix())

	def add_lap(self, n=1):
		self.lapCount += n
		self.stat['laps'] = self.lapCount

	def update_stat(self):
		json.dump(self.stat, self.statFile.open('w', encoding='utf-8'), indent=4)

def dump_data():
	with PICKLE_FILE.open('wb') as handle:
		pickle.dump(swimmers, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_data():
	global swimmers
	try: # Trying
		swimmers = pickle.load(PICKLE_FILE.open('rb'))
	except IOError: # When IOError Occurs
		swimmers = [] # Creating Empty Package List
		dump_data()
	except EOFError: # When EOFError Occurs
		swimmers = [] # Creating Empty Package List
		dump_data() # Call on SavePackageList Function

def init_data():
	global swimmers
	demo_names=		['Leonard Adelina',
					'Pooja Téo',
					'Muhammed Zion',
					'Dagrun Carmi',
					'Naime Rolo',
					'Nataša Gabrielle',
					'Mira Akhila',
					'Rajendra Jumanah',
					'Olgica Barbara',
					'Deòiridh Santino',
					'René Aurélio',
					'Stefania Gayathri',
					'Martha Benjamin',
					'Festus Phillipa',
					'Eliezer Ananth',
					'Jantine Gervasio',
					'Leon Maritza',
					'Theresa Sukhrab',
					'Menashe Simen',
					'Nour Balakrishna',
					'Nadia Sumeet',
					'Angus Calixto',
					'Amancio Josef',
					'Akhila Stoyanka']
	for i, name in enumerate(demo_names):
		swimmers.append(Swimmer(hex(2625070352 + i)[2:].upper(), name))

def generate_random_swimmer_data():
	num_detected = random.randint(0, len(swimmers))
	
	n = random.randint(0, 5)
	global scanned
	scanned = {}
	
	while n<len(swimmers):
		scanned[swimmers[n].uid] = -1 * random.randint(5, 100)
		n += random.randint(0, 3)
		
	print('print')
	print(json.dumps(scanned, sort_keys=True, indent=4))
	json.dump(scanned, SWIMMER_SCAN_FILE.open('w', encoding = 'utf-8'), indent=4)
		
def initialize_swimmer_data():
	global time_data
	time_data = {}
	for swimmer in swimmers:
		time_data[swimmer] = 0

def analyze_swimmer_data():
	with open(SWIMMER_SCAN_FILE) as json_file:
		scanned_data = json.load(json_file)
	print(scanned_data)
	for uid, strength in scanned_data.items():
		for swimmer, ticks in time_data.items():
			if swimmer.uid == uid:
				if (time.time() - ticks) > TIME_INTERVAL_BETWEEN_DETECTION	:
					if (strength < MAXIMUM_SIGNAL_STRENGTH) and (MINIMUM_SIGNAL_STRENGTH < strength):
						time_data[swimmer] = time.time()
						swimmer.add_lap()
						print('Lap added')


def clear_data():

	Confirmation=input('This will delete all data, ARE YOU SURE? (Y/N):').lower()
	if Confirmation=='y' or 'yes':
		try:
			os.remove('Swimmer_Database.pickle')
			shutil.rmtree('swimmers')
			os.remove('stat_all.json')
			os.remove('scanned.json')
			print('Files Deleted')
		except FileNotFoundError:
			print('Files Not Exist')
	else:
		print('Files NOT Deleted')

def add_swimmer():
	uid = input('UID: ')
	for swimmer in swimmers:
		if uid == swimmer.uid:
			print('Swimmer Exists.')
			return
	name = input('Name: ')
	for swimmer in swimmers:
		if name == swimmer.name:
			if (input('Swimmer Name Exists, proceed? (Y/N): ').upper() == 'N'):
				return
			break
	swimmers.append(Swimmer(uid, name))

def update_stat():
	allData = {}
	for swimmer in swimmers:
		json.dump(swimmer.stat, swimmer.statFile.open('w', encoding='utf-8'), indent=4)
		allData[swimmer.uid] = [swimmer.name, swimmer.lapCount]
	json.dump(allData, STAT_FILE.open('w', encoding='utf-8'), indent=4)
	dump_data()

def demo():
	while True:
		# chosenOne = random.choice(swimmers)
		# chosenOne.add_lap()
		# chosenOne.update_stat()
		generate_random_swimmer_data()
		analyze_swimmer_data()
		update_stat()
		time.sleep(random.uniform(1, 3))

if __name__ == '__main__':
	swimmers = []
	if '--clear-data' in sys.argv or '-c' in sys.argv:	
		clear_data()
		exit()
	elif not PICKLE_FILE.is_file():
		init_data()
	elif '--no-read' in sys.argv or '-n' in sys.argv:
		init_data()
	else:
		load_data()
	try:
		initialize_swimmer_data()
		demo()
	except KeyboardInterrupt:
		dump_data()
		print('Good bye')
