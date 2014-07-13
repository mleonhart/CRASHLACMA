from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home_page', name='home'),
    url(r'^about/$', 'main.views.about', name='about'),
    url(r'^map/', include('map.urls', namespace="map")),
    url(r'^browse/', include('browse.urls', namespace="browse")),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
