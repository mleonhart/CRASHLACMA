from django.conf.urls import patterns, url

from projection import views

urlpatterns = patterns('',
    url(r'^$', views.projection_home, name='projection_home')
)