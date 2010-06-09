from datetime import datetime

from django.contrib.gis.db import models
from core.models import Zone

# TODO: Creating classes to for geographical locations
#       and a class to hold police station respect to the
#       geographical location.

class Location(models.Model):
    """
        A Location is technically a geographical point/area (lat+long), but is often
       used to represent a large area such as a city or state.
     """
    name = models.CharField(max_length=100, help_text="Name of location")
    code = models.CharField(max_length=30, unique=True, blank=True, null=True)
    added_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(null=True, blank=True)
    
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.name


class Country(Location):
    """
        This is a country or states. eg Tanzania
    """
    area = models.PolygonField(blank=True)
    
    class Meta:
        verbose_name_plural = 'countries'

class Region(Location):
    """
        This sub division of the country eg Dar es salaam, Mwanza
    """
    country = models.ForeignKey(Country)
    area = models.PolygonField(blank=True)
    
class District(Location):
    """
        A sub-division of the region, 
    """
    region = models.ForeignKey(Region)
    area = models.PolygonField(blank=True)

class Ward(Location):
    """
        A sub-division of the district, 
    """
    region = models.ForeignKey(Region)
    area = models.PolygonField(blank=True)
    
class Station(Location):
    """
        A Station is a police station where crimes a reported.
    """
    ward = models.ForeignKey(Ward)
    zone = models.ForeignKey(Zone)

    point = models.PointField(blank=True)
    
    class Meta:
        verbose_name = "police station"
        verbose_name_plural = 'police stations'
