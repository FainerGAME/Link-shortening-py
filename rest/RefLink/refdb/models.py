from django.db import models

# Create your models here.
class RefDB(models.Model):
    fullurl = models.CharField(max_length=250,blank=True)
    shorturl = models.CharField(max_length=20,blank=True)
    
class Meta: 
    ordering = ('shorturl',)