from django.db import models
from investigation.models import *
import random

name_list=['John','Allen','Oswald','Auson','Gerald','Salome','Irene','Hildebrand','Mukulu','Hamis',
			'Paula','Gosbert','Jackson','Peter','Henry','Terence','Pius','Godfrey','Renatha','Humphrey',
			'Tumaini','Mbwana','Daniel','Adnan','Charles','Komba','Baraka','Oscar','Cosmas','Clement',
			'Pavati','Patel','Ramji','Husna','Lilian','Conrad','Jeremiah','Donald','David','Canicius',
			'Joseph','Silonda','Hanson','Yusuph','Ally','Bitego','Kagoma','Marium','Happy','Raymond',
			'Julius','Smith','Anderson','Lawrence']
occupation_list=['analyst','programmer','accountant','engineer','sales person','manager','proprietor',
				 'artist','musician','actor','rapper','cook','house wife','officer','driver','student',
				 'designer','comedian']
religion_list=['christian','budha','hindus','islam','pagan']

class Util():
	def resampleRegister(self,startnum,endnum):
		register = Register()
		for count in range(1,20):
			register.reportbook = ReportBook.objects.get(pk=random.randint(1,ReportBook.objects.count()))
			register.complainant = Complainant.objects.get(pk=random.randint(1,Complainant.objects.count()))
			register.property = Property.objects.get(pk=random.randint(1,Property.objects.count()))
			register.officer = Officer.objects.get(pk=random.randint(1,Officer.objects.count()))
			register.offense = Offense.objects.get(pk=random.randint(1,Offense.objects.count()))
			register.accused = Accused.objects.get(pk=random.randint(1,Accused.objects.count()))
			register.forensic = Forensic.objects.get(pk=random.randint(1,Forensic.objects.count()))
			register.results = Result.objects.get(pk=random.randint(1,Result.objects.count()))
			register.remarks = Remark.objects.get(pk=random.randint(1,Remark.objects.count()))
			register.court_case_number = count
			register.save()
			register = None
			register = Register()
	def resampleOfficer(self):
