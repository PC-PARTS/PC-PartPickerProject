from django.db import models
from django.contrib.auth.models import User

class Build(models.Model):
	
	cpu = models.CharField(max_length=100)
	cpu_cooler = models.CharField(max_length=100)
	motherboard = models.CharField(max_length=100)
	memory1 = models.CharField(max_length=100)
	memory2 = models.CharField(max_length=100,blank=True,null=True)
	storage1 = models.CharField(max_length=100)
	storage2 = models.CharField(max_length=100,blank=True,null=True)
	storage3 = models.CharField(max_length=100,blank=True,null=True)
	gpu = models.CharField(max_length=100)
	case = models.CharField(max_length=100)
	psu = models.CharField(max_length=100)
	os = models.CharField(max_length=100,blank=True,null=True)
	monitor1 = models.CharField(max_length=100,blank=True,null=True)
	monitor2 = models.CharField(max_length=100,blank=True,null=True)
	monitor3 = models.CharField(max_length=100,blank=True,null=True)
# Create your models here.
