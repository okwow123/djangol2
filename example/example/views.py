# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django.views.decorators.csrf import csrf_exempt
from .models import Store

@csrf_exempt    
def main(request):
    #store=Store.objects.all()
    #return render(request,'store/list.html',{'store':store})

    return render(request,'index.html',{})
