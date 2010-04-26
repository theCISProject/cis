from datetime import datetime

from django.db import models

# TODO: Creating classes to for geographical locations
#       and a class to hold police station respect to the
#       geographical location.

class LocationType(models.Model):
    """
	What do you mean by location type? make some clarifications here?
    """
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Location Type"

    def __unicode__(self):
        return self.name

class Location(models.Model):
    """A Location is technically a geographical point (lat+long), but is often
       used to represent a large area such as a city or state. It is recursive
       via the _parent_ field, which can be used to create a hierarchy (Country
       -> State -> County -> City) in combination with the _type_ field.
       rapidsms.locations
       """
       # TODO: lookup on recursion on django.
#    objects = RecursiveManager()
    type = models.ForeignKey(LocationType, related_name="locations", blank=True, null=True)
    name = models.CharField(max_length=100, help_text="Name of location")
    code = models.CharField(max_length=30, unique=True, blank=True, null=True)

    parent = models.ForeignKey("Location", related_name="children", null=True, blank=True,
        help_text="The parent of this Location. Although it is not enforced, it" +\
                  "is expected that the parent will be of a different LocationType")
    # TODO: add field for geo area position hint check out django. google maps

    def __unicode__(self):
        return self.name

class Station(models.Model):
    """
	A Station is a police station where crimes a reported.
    """
    name = models.CharField(max_length=80, help_text='Police Station name')
    code = models.CharField(max_length=80, blank=True, null=True)

    latitude  = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True, help_text="The physical latitude of this location")
    longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True, help_text="The physical longitude of this location")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Police Station"
