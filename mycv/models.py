from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    country_choices=[
    ('Nepal','Nepal'),
    ('India','India'),
    ('China','China'),
    ('Pakistan','Pakistan'),
    ('Bangladesh','Bangladesh'),
    ('USA','USA'),
    ('UK','UK'),


  ]
    
    image=models.ImageField(upload_to='profile')
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=60)
    DOB=models.DateField()
    nationality=models.CharField(max_length=50,choices=country_choices)
    github=models.URLField(max_length=50,blank=True)
    school=models.CharField(max_length=60)
    university=models.CharField(max_length=50)
    Graduated_year=models.DateField(blank=True)
    skills=models.TextField()
    about_you=models.TextField()
    Experience=models.TextField(blank=True)
    previous_work=models.TextField(blank=True) 
    
