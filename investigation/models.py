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
class Evidence(models.Model):
	REMARKS_CHOICES = (
		('1','Case Closed'),
		('2','Case Open'),
	)
	minute_sheet = models.TextField(verbose_name="Minute Sheet",blank=True)
	charge = models.TextField(verbose_name="Charges", blank=True)
	date = models.DateField(verbose_name="Date", blank=True)
	remark = models.CharField(verbose_name="Remark", max_length=80, choices=REMARKS_CHOICES, default=REMARKS_CHOICES[1],
								help_text="Status of the case, Closed/Not")
	rb_number = models.IntegerField(verbose_name="RB Number")
	#	Complainant is already in Investigation book (skipped)
	accused = models.ForeignKey(Accused)
	investigation_officer = models.CharField(verbose_name="Investigation Officer", max_length=80,
											 help_text="Name of officer investigating the case"
											 )
	total_value = models.IntegerField(verbose_name="Total Value", 
										help_text="Total value of properties"
										)
	criminal_case_number = models.IntegerField(verbose_name="Criminal Case number")
	
	
class Book(models.Model):
	ir_number = models.IntegerField(verbose_name="IR Number")
	rb_number = models.CharField(verbose_name="RB Number", max_length=80)
	complainant_name = models.CharField(verbose_name="Complainant Name", max_length=80)
	crime = models.CharField(verbose_name="Crime", max_length=80)
	detective_name = models.CharField(verbose_name="Detective Name", max_length=80)
	detective_signature = models.CharField(verbose_name="Detective Signature",max_length=80)
	evidence = models.ForeignKey(Evidence,verbose_name="Evidence", blank=True)
	
