import os
import random
import time
import shutil
import pickle

class Swimmer(object):
	"""docstring for Swimmer"""
	def __init__(self, UID='',Name='John Doe', Lap_Count=0):
		self.UID=UID
		self.Name=Name
		self.Lap_Count=Lap_Count
		if not os.path.exists('Swimmers/'+UID):
			os.makedirs('Swimmers/'+UID)
		shutil.copy('resources/Example_Swimmer/Certificate.html','Swimmers/'+UID)
		shutil.copy('resources/Example_Swimmer/index.html','Swimmers/'+UID)
		shutil.copy('resources/Example_Swimmer/Playground_Auth.html','Swimmers/'+UID)
		shutil.copy('resources/Example_Swimmer/Profile_Pic.jpg','Swimmers/'+UID)
	def Add_Lap(self,Add_Number=1):
		self.Lap_Count+=Add_Number

def Save():
	with open('Swimmer_Database.pickle', 'wb') as handle:
		pickle.dump(SwimmerList, handle, protocol=pickle.HIGHEST_PROTOCOL)

def Read():
	global SwimmerList
	try: # Trying

		with open('Swimmer_Database.pickle', 'rb') as handle:
			SwimmerList = pickle.load(handle) # Loading Package_List from File
	except IOError: # When IOError Occurs
		SwimmerList=[] # Creating Empty Package List
		Save() 
	except EOFError: # When EOFError Occurs
		SwimmerList=[] # Creating Empty Package List
		Save() # Call on SavePackageList Function

def AddSwimmer():
	UID=input('UID:')
	for i in SwimmerList:
		if(UID==i.UID):
			print('Swimmer Exists')
			return
	Name=input('Name:')
	for i in SwimmerList:
		if(Name==i.Name):
			if(input('Swimmer Name Exists, proceed? (Y or N):')=='N'):
				return
		else:
			SwimmerList.append(Swimmer(UID,Name))

def Update():
	Content='{'
	for i in SwimmerList:
		with open('Swimmers/'+i.UID+'/stat.json', mode='w', encoding='utf-8') as stat:
			stat.write('{\n\t"Name": "'+i.Name+'",\n\t"LapCount": '+str(i.Lap_Count)+',\n\t"UID": "'+i.UID+'"\n}')
		Content+='\n\t"'+i.UID+'":["'+i.Name+'", '+str(i.Lap_Count)+'],'
	Content=Content[:-1]
	Content+='\n}'
	with open('stat_all.json', mode='w', encoding='utf-8') as stat_all:
		stat_all.write(Content)
	Save()


def Demo():
	Demo_Name_List=['Leonard Adelina','Pooja Téo','Muhammed Zion','Dagrun Carmi','Naime Rolo','Nataša Gabrielle','Mira Akhila','Rajendra Jumanah','Olgica Barbara','Deòiridh Santino','René Aurélio','Stefania Gayathri','Martha Benjamin','Festus Phillipa','Eliezer Ananth','Jantine Gervasio','Leon Maritza','Theresa Sukhrab','Menashe Simen','Nour Balakrishna','Nadia Sumeet','Angus Calixto','Amancio Josef','Akhila Stoyanka']
	ID=0
	for b in SwimmerList:
		for i in Demo_Name_List:
		
			if(b.UID!="9C"+str(776510+ID)):
				SwimmerList.append(Swimmer("9C"+str(776510+ID),i))
			else:
				print('UID Exists')
		ID+=1
	while True:
		random.choice(SwimmerList).Add_Lap()
		Update()
		time.sleep(random.uniform(0,2))

Read()