from django.conf.urls import patterns, url

from browse import views

urlpatterns = patterns('',
    url(r'^$', views.browse_home, name='browse_home')
)