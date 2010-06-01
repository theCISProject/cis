#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from offenses.models import Offense

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
	offense = models.ForeignKey(Offense)
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
