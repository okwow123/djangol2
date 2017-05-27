# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
from store.models import Store


class Cmanage(models.Model):
    class Meta:
        unique_together = (('user_email', 'store_email'),)

    #cmanage_id = models.AutoField(primary_key=True,default=0)	
    user_email=models.CharField(max_length=50)
    store_email=models.ForeignKey(Store)


    #store_id = models.ForeignKey(User, unique=True)
    
    #store_email=models.CharField(max_length=50,primary_key=True)
    #user_email=models.CharField(max_length=50)
    #store_name=models.CharField(max_length=50)
    #store_address=models.CharField(max_length=50)
    #store_image=models.ImageField()
    #store_reward=models.IntegerField(default=0)
    #store_rdate = models.DateTimeField(auto_now_add=True, blank=True)
    
