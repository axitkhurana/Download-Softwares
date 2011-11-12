from django.db import models
from datetime import datetime
from resources import CATEGORY_CHOICES,CATEGORY_TUPLE,OS_CHOICES


# Create your models here.
class Software(models.Model):
    soft_name = models.CharField('Software Name', max_length = 30)
    description = models.TextField(null = True, blank=True)
    category = models.CharField(max_length = 80, choices = CATEGORY_TUPLE)
    subcategory = models.CharField(max_length = 80, choices = CATEGORY_CHOICES,
            null=True, blank=True) 
    #server side chek for sub cat & display only req sub cat using javascript
    tags = models.CharField(max_length=50,null=True,blank=True) 
    #save tags as a,b,c csv w/o spaces
    def __unicode__(self):
        return self.soft_name

class Operatingsys(models.Model):
    software = models.ForeignKey(Software)
    os_type = models.CharField(max_length=10, choices=OS_CHOICES) #os
    def __unicode__(self):
        return '%s %s' % (self.software.soft_name, self.os_type)

class Version(models.Model):
    version = models.CharField(max_length=20)
    operatingsys = models.ForeignKey(Operatingsys)
    link=models.CharField(max_length=100)
    date_added = models.DateTimeField('Date Added', default=datetime.now())
    size=models.DecimalField(max_digits=7, decimal_places=2,
            null=True,blank=True,default=None)	
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True,
            blank=True, default=None)
    download_count = models.IntegerField('No. of Downloads', default=0)
    uploaded_by = models.CharField('Uploaded By', max_length=20, null=True,
            blank=True)
    show = models.BooleanField(default=False)
    def __unicode__(self):
        return '%s %s %s' % (self.operatingsys.software.soft_name,
                self.operatingsys.os_type, self.version)
