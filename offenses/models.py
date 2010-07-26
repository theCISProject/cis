from django.db import models

class OffenseCategory(models.Model):
	SECTION_CHOICES = (
		('CRIMINAL','Criminal Offenses'),
		('TRAFFIC','Traffic Offenses'),
	)
	RANK_CHOICES = (
		('MAJOR','Major Offense'),
		('MINOR','Minor Offense'),
	)
	offense_section = models.CharField(max_length=20,help_text='Register offense category within criminal/traffic offenses',choices=SECTION_CHOICES,default=SECTION_CHOICES[0])
	rank = models.CharField(max_length=14,help_text='Rank crime category into major or minor crimes',choices=RANK_CHOICES,default=RANK_CHOICES[0])
	category_name = models.CharField(max_length=80, unique=True, help_text='Name of the Crime category, which shall rank Major/Minor')
	def __unicode__(self):
		''' Return crime categories and their sections'''
		return '%s' % (self.category_name)
	class Meta:
		verbose_name_plural = 'Offense Categories'

class Offense(models.Model):
	offense_category = models.ForeignKey(OffenseCategory,help_text='Specify Crime category where an Offense falls in, i.e "Major/Minor Traffic/Criminal Offenses".')
	offense_title = models.CharField(max_length=80,help_text='Register title of a newly established criminal/traffic offense.')
	def __unicode__(self):
		'''Return offense title'''
		return '%s' % (self.offense_title)
