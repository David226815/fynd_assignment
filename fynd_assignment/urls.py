from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

from fynd_assignment import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    url(r'^read_json', views.read_json, name='read_json'),

    url(r'^all_movies', views.all_movies, name='all_movies'),
]
