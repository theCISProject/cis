from django.db import models

class OffenseCategory(models.Model):
	SECTION_CHOICES = (
		(0,'Criminal Offenses'),
		(1,'Traffic Offenses'),
	)
	RANK_CHOICES = (
		(0,'Major Offense'),
		(1,'Minor Offense'),
	)
	offense_section = models.CharField(max_length=20,help_text='Register offense category within criminal/traffic offenses',choices=SECTION_CHOICES,default=SECTION_CHOICES[0])
	rank = models.CharField(max_length=14,help_text='Rank crime category into major or minor crimes',choices=RANK_CHOICES,default=RANK_CHOICES[0])
	category_name = models.CharField(max_length=80, unique=True, help_text='Name of the Crime category, which shall rank Major/Minor')
	def __unicode__(self):
		''' Return crime categories and their sections'''
		return '%s %s: %s' % (self.RANK_CHOICES[int(self.rank)][1].split()[0], self.SECTION_CHOICES[ int(self.offense_section) ][1],self.category_name)

class Offense(models.Model):
	offense_category = models.ForeignKey(OffenseCategory,help_text='Specify Crime category where an Offense falls in, i.e "Major/Minor Traffic/Criminal Offenses".')
	offense_title = models.CharField(max_length=80,help_text='Register title of a newly established criminal/traffic offense.')
	def __unicode__(self):
		'''Return offense title'''
		return '%s' % (self.offense_title)
