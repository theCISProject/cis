#!/usr/bin/env python
# -*- coding: utf-8 -*-

##	TODO:
##		- Meaning of criminal case number and how it's relataed to evidence
##		- RD(is it RB) number?
##		- Minute sheet carries what?
##		- Charge carries charges list or single charge?

from django.db import models
from cis.book.models import Accused

# Create your models here.
'''
	@ Doesn't have all information categories extracted from
	  last interview, there's category for forensic infos.
	  
	  Plus awaits Salome's categorization of crimes
'''

class Register(models.Model):
	ir_number = models.IntegerField('IR Number')
	rb_number = models.CharField(max_length=80)
	complainant = models.ForeignKey('Complainant')
	officer = models.ForeignKey('Officer')
	offense_category = models.CharField(max_length=80)
	offense_section = models.CharField(max_length=80)
	results = models.ForeignKey('Result')
	remarks = models.CharField(max_length=80)
	court_case_number = models.IntegerField('Court Case Number')

	
class Complainant(models.Model):
	name = models.CharField(max_length=80)
	age = models.IntegerField('Age')
	occupation = models.CharField(max_length=80)
	religion = models.CharField(max_length=80)
	tribe = models.CharField(max_length=80)
	residence = models.CharField(max_length=80)
	
class Property(models.Model):
	stollen = models.IntegerField('Worth of Stollen products')
	recovered = models.IntegerField('Worth of Recovered products')
	
	class Meta:
		verbose_name_plural = 'Properties'
	
class Officer(models.Model):
	name = models.CharField(max_length=80)
	position = models.CharField(max_length=80)

class Accused(models.Model):
	name = models.CharField(max_length=80)
	address = models.TextField(max_length=256, blank=True)
	age = models.IntegerField('Age')
	
	class Meta:
		verbose_name_plural = 'Accused'

class Result(models.Model):
	explanation = models.TextField(blank=True)
	date = models.DateField('Date')



"""
	@Old Compilation of investigation register
	have been commented below this text.
"""
#~ # Create your models here.
#~ class Evidence(models.Model):
	#~ REMARKS_CHOICES = (
		#~ ('1','Case Closed'),
		#~ ('2','Case Open'),
	#~ )
	#~ minute_sheet = models.TextField(verbose_name="Minute Sheet",blank=True)
	#~ charge = models.TextField(verbose_name="Charges", blank=True)
	#~ date = models.DateField(verbose_name="Date", blank=True)
	#~ remark = models.CharField(verbose_name="Remark", max_length=80, choices=REMARKS_CHOICES, default=REMARKS_CHOICES[1],
								#~ help_text="Status of the case, Closed/Not")
	#~ rb_number = models.IntegerField(verbose_name="RB Number")
	#~ #	Complainant is already in Investigation book (skipped)
	#~ accused = models.ForeignKey(Accused)
	#~ investigation_officer = models.CharField(verbose_name="Investigation Officer", max_length=80,
											 #~ help_text="Name of officer investigating the case"
											 #~ )
	#~ total_value = models.IntegerField(verbose_name="Total Value", 
										#~ help_text="Total value of properties"
										#~ )
	#~ criminal_case_number = models.IntegerField(verbose_name="Criminal Case number")
	#~ 
	#~ 
#~ class Book(models.Model):
	#~ ir_number = models.IntegerField(verbose_name="IR Number")
	#~ rb_number = models.CharField(verbose_name="RB Number", max_length=80)
	#~ complainant_name = models.CharField(verbose_name="Complainant Name", max_length=80)
	#~ crime = models.CharField(verbose_name="Crime", max_length=80)
	#~ detective_name = models.CharField(verbose_name="Detective Name", max_length=80)
	#~ detective_signature = models.CharField(verbose_name="Detective Signature",max_length=80)
	#~ evidence = models.ForeignKey(Evidence,verbose_name="Evidence", blank=True)
	#~ 
