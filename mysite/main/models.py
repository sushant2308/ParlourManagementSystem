from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone

class Services(models.Model):
    name=models.CharField(max_length=20, help_text='Enter the name of service')
    price=models.IntegerField(help_text='Enter the price of service')
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return self.name

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")
accept = [('Pending','Pending'),('Accepted','Accepted'),('Declined','Declined')]
choice = [(service.name,service.name) for service in Services.objects.all()]
class Appointment(models.Model):
    service = models.CharField(max_length=255,choices=choice)
    customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=255,choices=accept,default='Pending')
    date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    time= models.TimeField(null=True)

    def __str__(self):
         return self.service
    
  