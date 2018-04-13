import os
import random
import time
import shutil

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

SwimmerList=[]




def Update():
	os.system('rm -f stat_all.json')
	Content='{'
	for i in SwimmerList:
		with open('Swimmers/'+i.UID+'/stat.json', mode='w', encoding='utf-8') as stat:
			stat.write('{\n\t"Name": "'+i.Name+'",\n\t"LapCount": '+str(i.Lap_Count)+',\n\t"UID": "'+i.UID+'"\n}')
		Content+='\n\t"'+i.UID+'":["'+i.Name+'", '+str(i.Lap_Count)+'],'
	Content=Content[:-1]
	Content+='\n}'
	with open('stat_all.json', mode='w', encoding='utf-8') as stat_all:
		stat_all.write(Content)
def Demo():
	Demo_Name_List=['Leonard Adelina','Pooja Téo','Muhammed Zion','Dagrun Carmi','Naime Rolo','Nataša Gabrielle','Mira Akhila','Rajendra Jumanah','Olgica Barbara','Deòiridh Santino','René Aurélio','Stefania Gayathri','Martha Benjamin','Festus Phillipa','Eliezer Ananth','Jantine Gervasio','Leon Maritza','Theresa Sukhrab','Menashe Simen','Nour Balakrishna','Nadia Sumeet','Angus Calixto','Amancio Josef','Akhila Stoyanka']
	ID=0
	for i in Demo_Name_List:
		SwimmerList.append(Swimmer("9C"+str(776510+ID),i))
		ID+=1
	while True:
		random.choice(SwimmerList).Add_Lap()
		Update()
		time.sleep(random.uniform(0,2))