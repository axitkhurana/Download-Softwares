from django.db import models

# Create your models here.
MEDIA_CHOICES = (
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Radioo', (
            ('vhsdcasd', 'VHS Tape'),
            ('dvd', 'DdsVD'),
        )
    ),
    ('unknown', 'Unknownd'),
)
class delete(models.Model):
	media = models.CharField(max_length=20,choices=MEDIA_CHOICES)

#class delete_this(models.Model):
#	rating = models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True)
