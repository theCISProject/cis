#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from book.models import Report


class Information(models.Model):
    """
        Personal information
    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
#	One to many relationship, more than one person can
#	report same offense in the report book
#	We haven't account anonymity on offenses reporters some wants to
#	to be anonymouss
    report = models.ForeignKey(Report)
    name = models.CharField( verbose_name="Full name", max_length=80,help_text="Person's first, middle(if present) and last name")
    sex = models.CharField( verbose_name="Sex", max_length=6, choices= GENDER_CHOICES,help_text="Person's gender, Male/Female",default=GENDER_CHOICES[0])
    age = models.IntegerField( verbose_name="Age", max_length=3,help_text="Person's age")
    nationality = models.CharField( verbose_name="Nationality/Tribe", max_length=80,help_text="Person's Nationality or Tribe", default="Tanzanian",)
    occupation = models.CharField( verbose_name="Occupation", max_length=80,help_text="Person's Occupation/Job/Profession")
    postal_address = models.TextField(verbose_name="Postal Adress", blank=True,help_text="Person's Postal address (P.O.BOX)")
    # Suggested additional optional models to cope with technology
    # phone number, e_mail_adress & voter's id number
    #
    phone_number = models.CharField(verbose_name="Phone Number", blank=True, max_length=80,help_text="Person's Mobile phone number")
    e_mail = models.CharField(	verbose_name="E-Mail Adress", blank=True, max_length=80,help_text="Person's E-Mail address")
    voter_id = models.IntegerField( verbose_name="Voter's Id Number", blank=True, null=True, max_length=8,help_text="Identification number from your voter's id card")

    class Meta:
        verbose_name = "reporter's information"
        verbose_name_plural = "reporters' information"

    def __unicode__(self):
        information_summary= "Name: %s\nSex: %s\nAge: %s" % (self.name, self.sex, self.age )
        return information_summary
