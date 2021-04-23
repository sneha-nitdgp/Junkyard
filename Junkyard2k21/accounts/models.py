from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime, timedelta
from dateutil import tz

from django.conf import settings


# Create your models here.



class Team(models.Model):

    teamname = models.CharField(max_length=120)
    member1 = models.CharField(max_length=300)
    member1_phone = models.CharField(
        'Member1 Phone', max_length=25, blank=True)
    member2 = models.CharField(max_length=300)
    member2_phone = models.CharField(
        'Member2 Phone', max_length=25, blank=True)
    member3 = models.CharField(max_length=300)
    member4 = models.CharField(max_length=300)
    member3_phone = models.CharField(
        'Member3 Phone', max_length=25, blank=True)
    email = models.EmailField('Email Address', blank=True)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.teamname





