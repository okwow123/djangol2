# Create your models here.
from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import User

class Store(models.Model):
    store_email=models.CharField(max_length=50,primary_key=True)
    #store_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #store_id = models.ForeignKey(User, unique=True)
    #store_email = models.CharField(max_length=100)
    store_name=models.CharField(max_length=50)
    store_address=models.CharField(max_length=50)
    store_image=models.ImageField()
    store_reward=models.IntegerField(default=0)
