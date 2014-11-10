from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^imagr/', include('imagr.urls', namespace='imagr')),
    url(r'^admin/', include(admin.site.urls))
)
