from django.db import models
<<<<<<< HEAD
import operator


# Create your models here
class Post(models.Model):
	
	image=models.CharField(max_length=100, unique=False)
	title = models.CharField(max_length=100, unique=False)
	description= models.CharField(max_length=100, unique=False)
	author = models.CharField(max_length=100, unique=False)
        date = models.DateField(max_length=100, unique=False)
	date = models.DateField(max_length=100, unique=False)
	group = models.CharField(max_length=100, unique=False)


                

	def __unicode__(self):
		return '%s' %self.title


=======

# Create your models here
class Post(models.Model):
	title = models.CharField(max_length=100, unique=False)
	description= models.CharField(max_length=100, unique=False)
	author = models.CharField(max_length=100, unique=False)
	image=models.ImageField()
	def __unicode__(self):
		return '%s' %self.title
>>>>>>> 8bb6879efff4d6b1dd8ec3b3ff5a48ee6000e3f8
