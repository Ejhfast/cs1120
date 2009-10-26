from django.db import models
import datetime
# Create your models here.

class Story(models.Model):
	body = models.CharField(max_length=500)
	rating = models.IntegerField()
	orig_poster = models.CharField(max_length=15)
	post_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return self.body
		
	def was_posted_today(self):
		return self.post_date.date() == datetime.date.today()
	