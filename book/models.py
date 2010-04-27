#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
#from django.auth.models import User

#	TODO:
#		- Get sample data, to know data structures for the models
#		- Get Format of Monthly Serial Number
#		- Get Format of Investigation Number
#		- Get Format of Postal address recording
#		- Get Choices of Final disposal of report
#		- Get long form of PPR Number/meaning and format

class Report(models.Model):
    '''
        Report book from local police station
    '''

    CASE_STATUS_CHOICES= (
            ('Case Closed','Case Closed'),
            ('Case Opened','Case Opened'),
            ('Case Not Opened','Case Not Opened'),
    )
    serial_number = models.CharField( verbose_name="Monthly Serial Number", max_length=80,help_text="Report book number(RB) for reported crime")
    date = models.DateField(verbose_name="Date",help_text="Date of the reporting of crime")
    time = models.TimeField(verbose_name="Time",help_text="Time of the reporting of crime")
    #~ personal_information = models.OneToOneField(Information,verbose_name="Personal Informations",
                                                                                    #~ help_text="Information about the person reporting the crime")
    investigation_number = models.IntegerField(verbose_name="Investigation Number",null=True,help_text="Investigation number")
    property_detail = models.TextField(verbose_name="Properties details", blank=True,help_text="Found properties, its serial numbers and other references")
    # Status left instead of remarks field which carries
    # Status (case closed/not) and stamp of the police station
    status = models.CharField(verbose_name="Case status", max_length=80, choices=CASE_STATUS_CHOICES, blank=True,help_text="Case status Closed/Not",default=CASE_STATUS_CHOICES[2],)

    def __unicode__(self):
        return self.serial_number


class Detail(models.Model):
    '''
        Details of the report
    '''
    #	Needs expansion
    #	Type of crimes
    #   @response:: type of crimes check cis.offenses

    report_detail = models.OneToOneField(Report, verbose_name="Report Details")
    description = models.TextField(verbose_name="Description",help_text="Description of the reported crime")
    reporter_signature = models.CharField(verbose_name="Reporter's signature", max_length=80, help_text="Signature of the person reporting crime")
    officer_signature = models.CharField(verbose_name="Officer's signature", max_length=80, help_text="Signature of the officer receiveing the report")

    def __unicode__(self):
        return self.description

class Action(models.Model):
    '''
        Detailed information of action taken
    '''

    STATUS_CHOICES = (
        ('1','Immediate Action taken'),
        ('2','Investigation complete'),
        ('3','Awaiting action to be taken'),
    )

    FINAL_DISPOSAL_CHOICES = (
        ('1','N.F.A.'),
        ('2','Refused'),
        ('3','E.t.c.'),
    )
    action = models.ForeignKey(Report, verbose_name="Action details",blank=True)
    status = models.CharField(verbose_name="Status", max_length=80, choices=STATUS_CHOICES,help_text="Action status")
    officer_name = models.CharField(verbose_name="Officer's Name", max_length=80,help_text="Name of police officer taking initial action")
    final_disposal = models.CharField(verbose_name="Final Disposal", max_length=80, choices=FINAL_DISPOSAL_CHOICES,help_text="Final report disposal status")

    def __unicode__(self):
        return self.status

class Accused(models.Model):
    '''
        Person proceeding against
    '''
    GENDER_CHOICES= (
            ('M', 'Male'),
            ('F', 'Female'),
    )
    accused = models.ForeignKey(Report,blank=True)
    name = models.CharField( verbose_name="Full name", max_length=80,help_text="Person's first, middle(if present) and last name")
    sex = models.CharField( verbose_name="Sex", max_length=6, choices= GENDER_CHOICES,help_text="Person's gender, Male/Female")
    nationality = models.CharField( verbose_name="Nationality/Tribe", max_length=80,help_text="Person's Nationality or Tribe", default="Tanzanian")
    postal_address = models.TextField(verbose_name="Postal Adress", blank=True,help_text="Person's Postal address (P.O.BOX)")

    #   Suggested extra optional fields
    #~ occupation = models.CharField( verbose_name="Occupation", max_length=80,
                                                                    #~ help_text="Person's Occupation/Job/Profession"
                                                                    #~ )
    #~ phone_number = models.CharField(verbose_name="Phone Number", blank=True, max_length=80,
                                                                    #~ help_text="Person's Mobile phone number"
                                                                    #~ )
    #~ e_mail = models.CharField(	verbose_name="E-Mail Adress", blank=True, max_length=80,
                                                            #~ help_text="Person's E-Mail address"
                                                            #~ )

    class Meta:
        verbose_name_plural = 'accused'

    def __unicode__(self):
        return self.name

class Arrest(models.Model):
    '''
        Whether criminal has been arrested or not
    '''

    ARREST_CHOICES = (
            ('Arrested','Arrested'),
            ('Not Arrested','Not arrested'),
            ('Released','Released'),
    )

    arrest = models.ForeignKey(Report,blank=True)
    status = models.CharField(verbose_name="Status", max_length=80, choices=ARREST_CHOICES,help_text="Arrest status")
    name = models.CharField(verbose_name="Name", max_length=80,help_text="Name of person who arrested the accused")
    ppr_number = models.CharField(verbose_name="Name", max_length=80,help_text="P.P.R. Number")

    def isAccusedArrested(self):
        if self.status == '2':
            return False
        else:
            return True
