# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

class Cmanage(models.Model):
    store_email=models.CharField(max_length=50,primary_key=True)
    user_email=models.CharField(max_length=50)
    store_name=models.CharField(max_length=50)
    store_address=models.CharField(max_length=50)
    store_image=models.ImageField()
    store_reward=models.IntegerField(default=0)
    store_rdate = models.DateTimeField(auto_now_add=True, blank=True)
    
