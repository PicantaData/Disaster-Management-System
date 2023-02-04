from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=256)
    

class Skills(models.Model):
    name = models.CharField(max_length=64)

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=1,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Others')
        ])
    city = models.CharField(max_length=32)
    skills = models.ManyToManyField(Skills)
    
    
