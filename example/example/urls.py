from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^$',views.main,name='main'),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^store/', include('store.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
