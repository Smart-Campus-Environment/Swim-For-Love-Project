import random
import time
import shutil
from pathlib import Path
import pickle
import json
import sys

SWIMMERS_DIR = Path('Swimmers')
EXAMPLE_DIR = Path('resources/Example_Swimmer')
PICKLE_FILE = 'Swimmer_Database.pickle'
STAT_FILE = 'stat_all.json'

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
    with open(PICKLE_FILE, 'wb') as handle:
        pickle.dump(swimmers, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_data():
    global swimmers
    try: # Trying
        swimmers = pickle.load(open(PICKLE_FILE, 'rb'))
    except IOError: # When IOError Occurs
        swimmers = [] # Creating Empty Package List
        dump_data()
    except EOFError: # When EOFError Occurs
        swimmers = [] # Creating Empty Package List
        dump_data() # Call on SavePackageList Function

def init_data():
    global swimmers
    demo_names = ['Leonard Adelina',
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
    json.dump(allData, open(STAT_FILE, 'w', encoding='utf-8'), indent=4)

def demo():
    while True:
        chosenOne = random.choice(swimmers)
        chosenOne.add_lap()
        chosenOne.update_stat()
        update_stat()
        time.sleep(random.uniform(1, 3))

if __name__ == '__main__':
    swimmers = []
    try:
        if '--no-read' not in sys.argv and '-n' not in sys.argv:
            load_data()
        else:
            init_data()
        demo()
    except KeyboardInterrupt:
        dump_data()
        print('Good bye')
