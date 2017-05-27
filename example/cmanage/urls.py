from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^register_ok',views.register_ok,name='register_ok'),
]


