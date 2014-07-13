from django.conf.urls import patterns, url

from map import views

urlpatterns = patterns('',
    url(r'^$', views.map_home, name='map_home')
)