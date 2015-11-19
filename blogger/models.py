from django.db import models

# Create your models here
class Post(models.Model):
	title = models.CharField(max_length=100, unique=False)
	description= models.CharField(max_length=100, unique=False)
	author = models.CharField(max_length=100, unique=False)
	image=models.ImageField(max_lenght=100, unique=False)
	def __unicode__(self):
		return '%s' %self.title
