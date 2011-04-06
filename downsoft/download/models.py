from django.db import models

# Create your models here.
class Category(models.Model):
	category = models.CharField('Category Name',max_length=30)
	tags =  models.CharField(max_length=60) #check on maxlen of tag on upload by user
	def __unicode__(self):
		return self.category

class Software(models.Model):
	category = models.ForeignKey(Category)
	soft_name = models.CharField('Software Name',max_length=30) 
	rating = models.DecimalField(max_digits=3,decimal_places=2)
	tags = models.CharField(max_length=50)
	download_count = models.IntegerField('No. of Downloads')
	details = models.CharField(max_length=100) #|os;version;size|
	description = models.TextField()
	date_added = models.DateTimeField('Date Added')
	def __unicode__(self):
		return self.soft_name

class Comment(models.Model):
	software = models.ForeignKey(Software)
	comment = models.TextField()
	commented_by = models.CharField('Commented By',max_length=20)
	commment_time = models.DateTimeField('Comment Time')
	flag = models.BooleanField()
	flagged_by = models.CharField(max_length=20) #should be null when flag is false

class List(models.Model):
	list_name = models.CharField('List Name',max_length=3330)
	softwares = models.TextField()
