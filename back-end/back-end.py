'''
   _______          _______ __  __    ______ ____  _____     _      ______      ________
  / ____\ \        / /_   _|  \/  |  |  ____/ __ \|  __ \   | |    / __ \ \    / /  ____|
 | (___  \ \  /\  / /  | | | \  / |  | |__ | |  | | |__) |  | |   | |  | \ \  / /| |__
  \___ \  \ \/  \/ /   | | | |\/| |  |  __|| |  | |  _  /   | |   | |  | |\ \/ / |  __|
  ____) |  \  /\  /   _| |_| |  | |  | |   | |__| | | \ \   | |___| |__| | \  /  | |____
 |_____/    \/  \/   |_____|_|  |_|  |_|    \____/|_|  \_\  |______\____/   \/   |______|

'''

import random
import time
import shutil
import pickle
import json
import sys
import os
from config import *
from utils import *
from demo import *

logger = Logger('main')

class Swimmer:
    '''Base class for swimmers.'''

    def __init__(self, uid='', name='Anonymous', lapCount=0):
        self.uid = uid
        self.name = name
        self.lapCount = lapCount
        self.stat = {'name': self.name, 'uid': self.uid, 'laps': self.lapCount}
        self.dir = SWIMMERS_DIR / self.uid
        self.statFile = self.dir / 'stat.json'
        # Create player's directory
        if not self.dir.is_dir():
            shutil.copytree(EXAMPLE_DIR.as_posix(), self.dir.as_posix())

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

def init_data():
    '''Create names and add it to swimmers.'''
    global swimmers
    for i, name in enumerate(DEMO_NAMES):
        swimmers.append(Swimmer(hex(2625070352 + i)[2:].upper(), name))

def generate_random_swimmer_data():
    num_detected = random.randint(0, len(swimmers))

    n = random.randint(0, 5)
    global scanned
    scanned = {}

    while n<len(swimmers):
        scanned[swimmers[n].uid] = -1 * random.randint(5, 100)
        n += random.randint(0, 3)
    if Debug==1:
        logger.debug(json.dumps(scanned, sort_keys=True, indent=4))
    json.dump(scanned, SWIMMER_SCAN_FILE.open('w', encoding = 'utf-8'), indent=4)

def initialize_swimmer_data():
    global time_data
    time_data = {}
    for swimmer in swimmers:
        time_data[swimmer] = 0

def analyze_swimmer_data():
    if SWIMMER_SCAN_FILE.is_file():
        scanned_data = json.load(SWIMMER_SCAN_FILE.open(encoding='utf-8'))
    else:
        scanned_data = {}
    if Debug==1:
        logger.debug(scanned_data)
    for uid, strength in scanned_data.items():
        for swimmer, ticks in time_data.items():
            if swimmer.uid == uid:
                if (time.time() - ticks) > TIME_INTERVAL_BETWEEN_DETECTION  :
                    if (strength < MAXIMUM_SIGNAL_STRENGTH) and (MINIMUM_SIGNAL_STRENGTH < strength):
                        time_data[swimmer] = time.time()
                        swimmer.add_lap()
                        if Debug==1:
                            logger.debug('+'+swimmer.name+' Lap added')


def delete_data_files():
    '''Deletes all data files, including the pickle file,
    swimmers directories, stat_all.json, scanned.json'''
    confirm = input('This will delete all data files, proceed? [Y/N]: ')
    if confirm.upper() in ('Y', 'YES'):
        #########################################################
        ## NEEDS FIX, DELETE ONE AT A TIME, IF NOT FOUND, SKIP ##
        #########################################################
        try:
            os.remove('Swimmer_Database.pickle')
            shutil.rmtree('swimmers')
            os.remove('stat_all.json')
            os.remove('scanned.json')
            logger.info('Files Deleted')
        except FileNotFoundError:
            logger.warning('Files not found')
    else:
        logger.info('Files not deleted')

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
        if Debug==1:
            os.system('clear')
        generate_random_swimmer_data()
        analyze_swimmer_data()
        update_stat()
        time.sleep(random.uniform(1, 3))

if __name__ == '__main__':
    swimmers = []
    if '--debug' in sys.argv or '-d' in sys.argv:
        Debug=1
    else:
        Debug=0
    if '--clear-data' in sys.argv or '-c' in sys.argv:
        delete_data_files()
        exit()
    if '--help' in sys.argv or '-h' in sys.argv:
        print('''\n
-h  Show this help function
-n  Create new statistics
-c  Delete all swimmer files and statistics
-d  Show Debug Information (Verbose Output)\n\n''')
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
        logger.info('Good bye')
