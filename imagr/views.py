from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader


from imagr.models import Imagr_User, Photo, Album


def front(request):
    template = loader.get_template('imagr/front.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def home(request):
    album_list = Album.objects.all()
    template = loader.get_template('imagr/home.html')
    context = RequestContext(request, {
        'album_list': album_list
    })
    return HttpResponse(template.render(context))


def album(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404
    photos = album.photos.all()
    template = loader.get_template('imagr/album.html')
    context = RequestContext(request, {
        'album': album,
        'photos': photos
    })
    return HttpResponse(template.render(context))


def photo(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    template = loader.get_template('imagr/photo.html')
    context = RequestContext(request, {
        'photo': photo
    })
    return HttpResponse(template.render(context))


def stream(request):
    recent_photos = Photo.objects.order_by('date_published')[:10]
    template = loader.get_template('imagr/stream.html')
    context = RequestContext(request, {
        'recent_photos': recent_photos
        })
    return HttpResponse(template.render(context))
