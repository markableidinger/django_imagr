from django.conf.urls import patterns, url

from imagr.views import home, front, stream, album, photo

urlpatterns = patterns('',
    url(r'^$', front, name='front'),
    url(r'^home/$', home, name='home'),
    url(r'^stream/$', stream, name='stream'),
    url(r'^album/(?P<album_id>\d+)/$', album, name='album'),
    url(r'^photo/(?P<photo_id>\d+)/$', photo, name='photo')
)
