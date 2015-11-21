from django.db import models
import operator


# Create your models here
class Post(models.Model):
	counter = models.IntegerField()	
	image=models.CharField(max_length=100, unique=False)
	title = models.CharField(max_length=100, unique=False)
	description= models.CharField(max_length=100, unique=False)
	author = models.CharField(max_length=100, unique=False)
        date = models.DateField(max_length=100, unique=False)
	date = models.DateField(max_length=100, unique=False)
	group = models.CharField(max_length=100, unique=False)


                

	def __unicode__(self):
		return '%s' %self.title


