"""homeserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^upload/$',views.upload,name="upload"),
    url(r'^uploads/(?P<id>[0-9]+)/$',views.download_wo_authenticate, name="download"),
    url(r'^authenticate/(?P<id>[0-9]+)/$', views.authenticate, name="authenticate"),
    url(r'^view/$', views.view_file, name="view"),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete_file, name="delete"),
    url(r'^display/(?P<id>[0-9]+)/$', views.display_file, name="display"),
    url(r'^play/(?P<id>[0-9]+)/$', views.play_music, name="display")
]
