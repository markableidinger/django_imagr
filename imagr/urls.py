from django.conf.urls import patterns, url

from imagr.views import profile, front, stream, album, photo, profile_redirect

urlpatterns = patterns('',
    url(r'^$', front, name='front'),
    url(r'^profile/(?P<user_id>\d+)/$', profile, name='profile'),
    url(r'^stream/$', stream, name='stream'),
    url(r'^album/(?P<album_id>\d+)/$', album, name='album'),
    url(r'^photo/(?P<photo_id>\d+)/$', photo, name='photo'),
    url(r'^profile/$', profile_redirect, name='profile_redirect')
)
