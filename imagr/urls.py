from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from imagr.views import profile, front, stream, album, photo, profile_redirect, photo_redirect, follow, make_album, set_cover

urlpatterns = patterns('',
    url(r'^$', front, name='front'),
    url(r'^profile/(?P<user_id>\d+)/$', profile, name='profile'),
    url(r'^stream/$', stream, name='stream'),
    url(r'^album/(?P<album_id>\d+)/$', album, name='album'),
    url(r'^photo/(?P<photo_id>\d+)/$', photo, name='photo'),
    url(r'^profile/$', profile_redirect, name='profile_redirect'),
    url(r'^photo/image/(?P<photo_id>\d+)/$', photo_redirect, name='photo_redirect'),
    url(r'^profile/follow/(?P<user_id>\d+)/$', follow, name='follow'),
    url(r'^profile/makealbum/(?P<user_id>\d+)/$', make_album, name ='make_album'),
    url(r'^album/cover/(?P<album_id>\d+)/(?P<photo_id>\d+)/$', set_cover, name='set_cover'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
