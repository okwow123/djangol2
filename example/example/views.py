# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django.views.decorators.csrf import csrf_exempt
#from .models import Store
#from django.db import models
from store.models import *

@csrf_exempt    
def main(request):
    if request.POST.get('storesearch')==None:
        store=Store.objects.all()
    else:
        store=Store.objects.filter(store_name=request.POST.get('storesearch'))

    return render(request,'index.html',{'store':store})

    
    #return render(request,'index.html',{})
