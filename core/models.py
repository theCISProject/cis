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
    description = models.TextField()

    # Propose to add a head to each zone to validate data
    # submittion in their zone.. EXPERIMENTAL! (allen)
    # head = models.ForeignKey(Police)
    # TODO:  Add more relevant fields

    def __unicode__(self):
        return self.name

class PoliceProfile(User):
    """
        A Web ui user, who can see data or be and administrator.
    """
    
    # These roles do not depict real roles are just layed as sample
    # and shuld be change ASAP.!
    ROLES_CHOICES = (
        ('ADM', 'Administrator'),
        ('PR', 'Police Reporter'),
        ('PA', 'Police Analyser'),
        ('MN', 'Manager'),
    )

    zone = models.ForeignKey(Zone)
    # TODO: put a level feature apart from the one provided by
    # django(admin, staff, active). eg Police reporter, Analyser, ...
    Role = models.CharField(max_length=3, choices=ROLES_CHOICES)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)