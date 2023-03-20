from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
# Create your models here.


class User(AbstractUser):

    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    phone = models.BigIntegerField(unique=True,default=None,null=True)
    college= models.CharField(max_length=200,null=True,blank=True)
    password = models.CharField(max_length=500)
    year_of_study = models.CharField(max_length=10,default=None,null=True)
    events_registered = models.IntegerField(default=0,null=True)
    flag = models.IntegerField(default=0)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class TypeOfEvent(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Events(models.Model):
    event_name = models.CharField(max_length=30)
    event_type = models.ForeignKey(TypeOfEvent,null=True,on_delete=models.CASCADE)
    event_fee = models.IntegerField()
    event_description = models.TextField()
    event_prize_money= models.IntegerField(null=True,default=None,blank=True)
    event_runner_prize_money= models.IntegerField(null=True,default=None,blank=True)
    event_cordinator1 = models.CharField(max_length=30,null=True,default=None,blank=True)
    event_cordinator2 = models.CharField(max_length=30,null=True,default=None,blank=True)
    event_cordinator3 = models.CharField(max_length=30,null=True,default=None,blank=True)
    event_cordinator4 = models.CharField(max_length=30,null=True,default=None,blank=True)
    team_size = models.IntegerField(null=True,default=None,blank=True)
    event_poster = models.ImageField(upload_to='uploads')
    
    def __str__(self):
        return self.event_name


class Registrations(models.Model):
    user = models.IntegerField()
    event = models.IntegerField()
    amount = models.IntegerField(null=True, blank=True)
    checksum = models.CharField(max_length=1000, null=True, blank=True)
    payment = models.BooleanField(null=True, blank=True)


    