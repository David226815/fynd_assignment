from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

from rest_framework.urlpatterns import format_suffix_patterns
from movies import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    url(r'^movies/', views.movieslist.as_view()),

    url(r'^read_json', views.read_json, name='read_json'),
    url(r'^all_movies', views.all_movies, name='all_movies'),
]
