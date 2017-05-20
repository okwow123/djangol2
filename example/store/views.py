# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Store
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django.views.decorators.csrf import csrf_exempt


def list(request):
    store=Store.objects.all()
    return render(request,'store/list.html',{'store':store})
    
def register(request):
    return render(request,'store/register.html',{})

@csrf_exempt
def register_ok(request):
    qs=Store.objects.exclude(store_email=request.POST.get('store_email'))
    if request.method=='POST' and qs.exists():
        store=Store.objects.create(
            store_email=request.POST.get('store_email'),
            #store_id_id=request.POST.get('store_id_id'),
            store_name=request.POST.get('store_name'),
            store_address=request.POST.get('store_address'),
            store_image=request.POST.get('store_image'),
            store_reward=request.POST.get('store_reward'),
        )
    return render(request,'store/register_ok.html',{})

def manage(request):
    return render(request,'store/manage.html',{})

