from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    user_type=models.CharField(max_length=10)
class carrental(models.Model):
    pickuplocation=models.CharField(max_length=30)
    pickupdate=models.CharField(max_length=30)
    pickuptime=models.CharField(max_length=30)
    dropofflocation=models.CharField(max_length=30)
    dropoffdate=models.CharField(max_length=30)
    dropofftime=models.CharField(max_length=30)
   
   
class mechanic(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    work_duration=models.CharField(max_length=30,default='')
    salary=models.CharField(max_length=30)
    





