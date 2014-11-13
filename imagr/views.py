from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone
from imagr.models import Imagr_User, Photo, Album
from forms import UploadFileForm, CreateAlbumForm
import boto
from boto.s3.key import Key

def front(request):
    template = loader.get_template('imagr/front.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def profile_redirect(request):
    logged_in_user = request.user
    return HttpResponseRedirect('/imagr/profile/{}'.format(logged_in_user.id))

def profile(request, user_id):
    logged_in_user = request.user
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            albuminfo = form.cleaned_data
            title = albuminfo['title']
            published = albuminfo['published']
            date_published = timezone.now()
            date_uploaded = timezone.now()
            date_modified = timezone.now()
            owner_id = logged_in_user.id
            new_album = Album(title=title, published=published, date_modified=date_modified,
                date_published=date_published, date_uploaded=date_uploaded, owner_id=owner_id)
            new_album.save()
            return HttpResponseRedirect('/imagr/profile/{}'.format(logged_in_user.id))
    else:
        logged_in_user = request.user
        album_list = Album.objects.filter(owner_id = logged_in_user.id)
        # album_list = [album for album in album_list if album.id == logged_in_user.id]
        template = loader.get_template('imagr/profile.html')
        context = RequestContext(request, {
            'album_list': album_list,
            'user': logged_in_user,
            'form': CreateAlbumForm
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
    conn = boto.connect_s3
    bucket = conn.get_bucket('imagrphotostorage')
    k = Key(bucket)
    k.key = photo_id
    picture = k.get_file()
    photo = Photo.objects.get(pk=photo_id)
    template = loader.get_template('imagr/photo.html')
    context = RequestContext(request, {
        'photo': photo,
        'picture': picture
    })
    return HttpResponse(template.render(context))
"""
take the picture from get_file() and find meta data related to content type 
and content length.
create a new url associated with the image like photo/image/1
and a view. but it does not need to have a template. 
build a response object and return

"""

def stream(request):
    recent_photos = Photo.objects.order_by('date_published')[:10]
    template = loader.get_template('imagr/stream.html')
    context = RequestContext(request, {
        'recent_photos': recent_photos
        })
    return HttpResponse(template.render(context))

