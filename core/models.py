from datetime import datetime

from django.db import models

from locations.models import Station

class StationPolice(models.Model):
    """
        A police working in a police station and he/she is 
        responsible of reporting the crime reported to his/her
        police station.
    """
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    police_code = models.CharField(max_length=255, help_text="A police ID number")
    
    # date added/modified of the police user.
    created_date = models.DateTimeField(default=datetime.now)
    edited_date = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.username

class PoliceProfile(models.Model):
    """
        Profile for the police working on the station
        with extra details.
        One profile to a single police.
    """
    police = models.ForeignKey(StationPolice, unique=True)
    station = models.ForeignKey(Station)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    
    created_date = models.DateTimeField(default=datetime.now)
    edited_date = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return "%s at %s" % (self.police, self.station)