from django.db import models

class Category(models.Model):
    """
        Holds name of offenses category like
        and a type of the offenses whether major crime or minor crime
    """
    TYPE_CHOICES = (
        ('major', 'Major Crime'),
        ('minor', 'Minor Crime'),
    )
    
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80,choices=TYPE_CHOICES)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class Offense(models.Model):
    """
        Crime holds the name of the crime and category it falls
        into such as road accident, stealing, counterfits
    """

    name =  models.CharField(max_length=80)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name
