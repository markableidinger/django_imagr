from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone
from imagr.models import Imagr_User, Photo, Album
from forms import UploadFileForm
import boto
from boto.s3.key import Key

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
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print "made it to views"
            photoinfo = form.cleaned_data
            ### make new photo ###
            title = photoinfo['title']
            published = photoinfo['published']
            date_published = timezone.now()
            date_uploaded = timezone.now()
            date_modified = timezone.now()
            owner_id = 1
            new_photo = Photo(title=title, published=published, date_published=date_published,\
            date_modified=date_modified, date_uploaded=date_uploaded, owner_id=owner_id)
            new_photo.save()
            new_photo.album_set.add(album_id)
            this_album = Album.objects.get(pk=album_id)
            id = new_photo.id
            this_album.photos.add(id)
            handle_uploaded_file(request.FILES['file'], id)
            return HttpResponseRedirect('/imagr/album/{}'.format(album_id))
        else:
            return HttpResponseRedirect('/imagr/album/{}'.format(album_id))
    else:
        try:
            album = Album.objects.get(pk=album_id)
        except Album.DoesNotExist:
            raise Http404
        photos = album.photos.all()
        template = loader.get_template('imagr/album.html')
        context = RequestContext(request, {
            'album': album,
            'photos': photos,
            'form': UploadFileForm
        })
        return HttpResponse(template.render(context))

def handle_uploaded_file(f, id):
    # url = 'http://imagrphotostorage.s3-website-us-west-2.amazonaws.com/'
    conn = boto.connect_s3()
    bucket = conn.get_bucket('imagrphotostorage')
    k = Key(bucket)
    k.key = id
    k.set_contents_from_file(f)

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

