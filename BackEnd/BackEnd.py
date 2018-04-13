import os
import random
import time

class Swimmer(object):
	"""docstring for Swimmer"""
	def __init__(self, UID='',Name='John Doe', Lap_Count=0):
		self.UID=UID
		self.Name=Name
		self.Lap_Count=Lap_Count
	def Add_Lap(self,Add_Number=1):
		self.Lap_Count+=Add_Number

SwimmerList=[]

def WriteLine(Content):
	with open('stat_all.json', mode='at', encoding='utf-8') as stat_all:
		stat_all.write(Content)


def Update():
	os.system('rm -f stat_all.json')
	WriteLine('{ ')
	for i in SwimmerList:
		WriteLine('\n"'+i.UID+'":["'+i.Name+'", '+str(i.Lap_Count)+'],')
	os.system("sed -i '' '$! { P; D; }; s/.$//' stat_all.json")
	WriteLine('} ')

def Demo():
	Demo_Name_List=['Leonard Adelina','Pooja Téo','Muhammed Zion','Dagrun Carmi','Naime Rolo','Nataša Gabrielle','Mira Akhila','Rajendra Jumanah','Olgica Barbara','Deòiridh Santino','René Aurélio','Stefania Gayathri','Martha Benjamin','Festus Phillipa','Eliezer Ananth','Jantine Gervasio','Leon Maritza','Theresa Sukhrab','Menashe Simen','Nour Balakrishna','Nadia Sumeet','Angus Calixto','Amancio Josef','Akhila Stoyanka']
	ID=0
	for i in Demo_Name_List:
		SwimmerList.append(Swimmer("9C"+str(776510+ID),i))
		ID+=1
	while True:
		random.choice(SwimmerList).Add_Lap()
		Update()
		time.sleep(0.6)