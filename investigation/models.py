#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from offenses.models import Offense
from locations.models import Station

# Create your models here.
'''
	@ Doesn't have all information categories extracted from
	  last interview, there's category for forensic infos.
	  
	  Plus awaits Salome's categorization of crimes
'''

class Register(models.Model):
	ir_number = models.IntegerField('IR Number',help_text="Investigation Number, Integer counts from 1 yearly")
	rb_number = models.ForeignKey('ReportBook',help_text="Report book number,[Number/Date]")
	complainant = models.ForeignKey('Complainant',help_text="Details of complainant")
	property = models.ForeignKey('Property',help_text="Stolen and recovered property's worth")
	officer = models.ForeignKey('Officer',help_text="Officer's details [Name & Position]")
	offense = models.ForeignKey(Offense, help_text="Offense title and category the Offense falls in")
	accused = models.ForeignKey('Accused',help_text="Information of the accused individual")
	forensic = models.ForeignKey('Forensic',null=True,blank=True,help_text="Forensic Information (if any)")
	results = models.ForeignKey('Result',help_text="Results of investigation [Explanation]")
	remarks = models.ForeignKey('Remark',help_text="How the case ended, or where it reached")
	court_case_number = models.IntegerField(blank=True,null=True,help_text='Court case Number if case was opened')
	def __unicode__(self):
		return 'IR Number: %d    Complainant %s' % ( self.ir_number, self.complainant)

class Remark(models.Model):
	description = models.CharField(max_length=80,help_text="How the case ended,e.g. On-going Invest., On-Trial,Case Closed")
	def __unicode__(self):
		return '%s' % (self.description)

class ReportBook(models.Model):
	station = models.OneToOneField(Station,help_text="Police Station Where Offence was registered")
	book_date = models.DateField(help_text="Date of the report book where offense is registered")
	ir_number = models.IntegerField(help_text="IR Number of the dated report book in police station")
	def __unicode__(self):
		return 'Station:%s IR Number:%d' % (self.station, self.ir_number)

class Forensic(models.Model):
	tcro_number = models.IntegerField(help_text="TCRO Number from Forensic database")
	dispatch_date = models.DateField(help_text="Dispatch date of finger prints")
	return_date = models.DateField(help_text="Return date of finger prints")
	def __unicode__(self):
		return 'Forensic info in TCRO Number:%d' % (self.tcro_number)

class Accused(models.Model):
	GENDER_CHOICES= (
            ('M', 'Male'),
            ('F', 'Female'),
    )
	first_name = models.CharField(max_length=80,help_text="First name of Accused")
	last_name = models.CharField(max_length=80, help_text="Surname (and middle name if any)")
	address = models.TextField(blank=True,null=True,help_text="Plance of residence of accused")
	age = models.IntegerField(help_text="Age of the accused")
	gender = models.CharField(max_length=10,choices=GENDER_CHOICES,help_text="Gender of Accused [Male/Female]")
	nationality = models.CharField(max_length=80,help_text="Nationality/Tribe [Tribe if Tanzanian]")
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)
	
class Complainant(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	age = models.IntegerField('Age')
	occupation = models.CharField(max_length=80)
	religion = models.CharField(max_length=80)
	tribe = models.CharField(max_length=80,help_text="Tribe of individual")
	residence = models.TextField(max_length=80,help_text="Place of residence of complainant[Country/Region/District/Municipal/Ward/Street/Village")
	def __unicode__(self):
		return 'Name :%s %s   Age: %d' % (self.first_name, self.last_name, self.age)
	
class Property(models.Model):
	stollen = models.IntegerField('Worth of Stollen products')
	recovered = models.IntegerField('Worth of Recovered products')
	def __unicode__(self):
		return 'Stollen: %s    Recovered: %s' % (self.stollen, self.recovered)
	
	class Meta:
		verbose_name_plural = 'Properties'
	
class Officer(models.Model):
	name = models.CharField(max_length=80)
	position = models.CharField(max_length=80)
	def __unicode__(self):
		return 'Name: %s    Position: %s' % (self.name, self.position)

class Accused(models.Model):
	name = models.CharField(max_length=80)
	address = models.TextField(max_length=256, blank=True)
	age = models.IntegerField('Age')
	def __unicode__(self):
		return 'Name: %s    Address: %s' % (self.name, self.address)
	
	class Meta:
		verbose_name_plural = 'Accused'

class Result(models.Model):
	explanation = models.TextField(blank=True,help_text="Explanations on results of the investigation")
	date = models.DateField('Date')
	def __unicode__(self):
		return '%s    Date :%s' % (self.explanation, self.date)
