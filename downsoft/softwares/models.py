from django.db import models
from datetime import datetime
from resources import CATEGORY_CHOICES,CATEGORY_TUPLE,OS_CHOICES

# Create your models here.
class Software(models.Model):
	soft_name = models.CharField('Software Name',max_length=30)
	link=models.CharField(max_length=100)
	date_added = models.DateTimeField('Date Added',default=datetime.now())
	size=models.DecimalField(max_digits=7,decimal_places=2)	
	os = models.CharField(max_length=10,choices=OS_CHOICES)
	version = models.CharField(max_length=20)
	description = models.TextField(null=True,blank=True)
	category = models.CharField(max_length=80,choices=CATEGORY_TUPLE)
	subcategory = models.CharField(max_length=80,choices=CATEGORY_CHOICES,null=True,blank=True)# server side chek for sub cat & display only req sub cat using javascript
	tags = models.CharField(max_length=50,null=True,blank=True)
	rating = models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True,default=None)
	download_count = models.IntegerField('No. of Downloads',default=0)
	uploaded_by = models.CharField('Uploaded By',max_length=20,null=True,blank=True)
	show = models.BooleanField(default=False)
	def __unicode__(self):
		return self.soft_name

class Comment(models.Model):
	software = models.ForeignKey(Software)
	comment = models.TextField()
	commented_by = models.CharField('Commented By',max_length=20)
	commment_time = models.DateTimeField('Comment Time')
	flag = models.BooleanField()
	flagged_by = models.CharField(max_length=80,null=True) #should be null when flag is false and in form of a list
	def __unicode__(self):
		return self.comment

#class List(models.Model):
#	list_name = models.CharField('List Name',max_length=3330)
#	softwares = models.TextField()
