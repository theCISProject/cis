from django.db import models

#TODO:  Re-think on the overall structure of this model.


class Category(models.Model):
    """
        Holds name of offenses category like
        and a type of the offenses whether major crime or minor crime
    """
    name = models.CharField(max_length=80)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

class Offense(models.Model):
    """
        Crime holds the name of the crime, type and category it falls
        into such as road accident, stealing, counterfits
    """
    TYPE_CHOICES = (
        ('major', 'Major Crime'),
        ('minor', 'Minor Crime'),
    )

    name =  models.CharField(max_length=80)
    category = models.ForeignKey(Category)
    type = models.CharField(max_length=80,choices=TYPE_CHOICES)

    def __unicode__(self):
        return self.name