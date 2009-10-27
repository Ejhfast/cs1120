from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm 
import datetime

class Story(models.Model):
	body = models.CharField(max_length=500)
	rating = models.IntegerField()
	orig_poster = models.CharField(max_length=15)
	post_date = models.DateTimeField('date published', auto_now=True)
	
	def __unicode__(self):
		return self.body
		
	def was_posted_today(self):
		return self.post_date.date() == datetime.date.today()

class StoryForm(ModelForm):
	class Meta:
		model = Story

class UserForm(ModelForm):
	class Meta:
		model = User
		exclude = ['groups','user_permissions','is_superuser', 'last_login', 'date_joined', 'is_active', 'is_staff']
	
