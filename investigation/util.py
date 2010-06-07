from django.db import models
from investigation.models import *
import random

class Util():
	def resample(self,startnum,endnum):
		register = Register()
		for count in range(5,60):
			register.ir_number = count
			register.rb_number = ReportBook.objects.get(pk=random.randint(1,ReportBook.objects.count()))
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
