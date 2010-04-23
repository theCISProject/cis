from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

# TODO: the core app for cis, data-loc privialages, user access privillages,

class Zone(models.Model):
    """
        Zone highest level collection of people/stuff
        in the system.  Pretty much everything happens at the
        zone-level, including user membership, permission to
        see data, reports, charts, etc.
    """
    name  = models.CharField(max_length=64, unique=True)
    # TODO:  Add more relevant fields

    def __unicode__(self):
        return self.name