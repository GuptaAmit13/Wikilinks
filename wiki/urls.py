"""wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include,url 
from django.contrib import admin
from wikilinks import views

urlpatterns=[
url(r'^$','wikilinks.views.home'),
url(r'^admin/',include(admin.site.urls)),
url(r'^index/',views.index),
url(r'^login/',views.return_login),
url(r'^question/',views.question),
url(r'^wiki/',views.game),
url(r'^time/',views.get_time),
url(r'^timeup/',views.get_timeup),
#url(r'^wiki/timeup/',views.get_timeup),
#url(r'^(?P<q_id>\d+)/$',views.question)
]

