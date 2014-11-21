from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone
from imagr.models import Imagr_User, Photo, Album
from forms import UploadFileForm, CreateAlbumForm, FollowerForm
import boto
import re
from boto.s3.key import Key
from django.db.models import Q

def front(request):
    template = loader.get_template('imagr/front.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def profile_redirect(request):
    logged_in_user = request.user
    return HttpResponseRedirect('/imagr/profile/{}'.format(logged_in_user.id))

def make_album(request, user_id):
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
            return HttpResponse("Sorry, we couldn't process your request")
    else:
        return HttpResponse('Access Denied')

def profile(request, user_id):
    logged_in_user = request.user
    album_list = Album.objects.filter(owner_id = user_id)
    # album_list = [album for album in album_list if album.id == logged_in_user.id]
    template = loader.get_template('imagr/profile.html')
    context = RequestContext(request, {
        'album_list': album_list,
        'user': logged_in_user,
        'page_owner': Imagr_User.objects.get(pk=user_id),
        'form': CreateAlbumForm,
        'followform': FollowerForm
    })
    return HttpResponse(template.render(context))


def album(request, album_id):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            photoinfo = form.cleaned_data
            ### make new photo ###
            title = photoinfo['title']
            published = photoinfo['published']
            date_published = timezone.now()
            date_uploaded = timezone.now()
            date_modified = timezone.now()
            owner_id = request.user.id
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
        logged_in_user = request.user
        album_owner = Imagr_User.objects.get(pk=(album.owner.id))
        context = RequestContext(request, {
            'album': album,
            'photos': photos,
            'form': UploadFileForm,
            'logged_in_user': logged_in_user,
            'album_owner': album_owner
        })
        return HttpResponse(template.render(context))

def handle_uploaded_file(f, id):
    # url = 'http://imagrphotostorage.s3-website-us-west-2.amazonaws.com/'
    conn = boto.connect_s3()
    name, extension = str(f).split('.')
    bucket = conn.get_bucket('imagrphotostorage')
    bucket_location = bucket.get_location()
    if bucket_location:
        conn = boto.s3.connect_to_region(bucket_location)
        bucket = conn.get_bucket('imagrphotostorage')
    k = Key(bucket)
    k.key = id
    content_type = 'image/' + extension
    k.set_metadata('Content-Type', content_type)
    k.set_contents_from_file(f)

def photo(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    template = loader.get_template('imagr/photo.html')
    context = RequestContext(request, {
        'photo': photo,
    })
    if photo.published == 'private' and photo.owner.id != request.user.id:
        return HttpResponse('You do not have access to this content')
    elif photo.published == 'shared':
        viewer = request.user
        owner = photo.owner
        if photo.owner == request.user:
            return HttpResponse(template.render(context))
        try:
            user_confirm = viewer.following.get(id=owner.id)
            other_user_confirm = owner.following.get(id=viewer.id)
            return HttpResponse(template.render(context))
        except:
            return HttpResponse('You must follow this user first')
    else:
        return HttpResponse(template.render(context))

def photo_redirect(request, photo_id):
    conn = boto.connect_s3()
    bucket = conn.get_bucket('imagrphotostorage')
    k = Key(bucket)
    k.key = photo_id
    picture = k.get_contents_as_string()
    file_type = k.get_metadata('Content-Type')
    response = HttpResponse(picture, content_type=file_type)
    return response

def follow(request, user_id):
    print request.user
    print request.user.id
    print user_id
    if str(request.user.id) == str(user_id):
        if request.method == 'POST':
            form = FollowerForm(request.POST)
            following_user = Imagr_User.objects.get(id=user_id)
            is_valid = form.is_valid()
            print is_valid
            if is_valid:
                data = form.cleaned_data
                followed = data['username']
                print followed
                try:
                    followed_user = Imagr_User.objects.get(username=followed)
                    print followed_user
                    print type(following_user)

                    try:
                        confirm_user = following_user.following.get(username=followed_user.username) 
                        print "following relation exists, found :", confirm_user
                    except:
                        print "adding to following list"
                        following_user.following.add(followed_user.id)
                    return HttpResponseRedirect('/imagr/profile/{}'.format(followed_user.id))
                except:
                    print 'raised an error'
                    return HttpResponseRedirect('/imagr/profile/{}'.format(user_id))
        else:
            return HttpResponseRedirect('/imagr/profile/{}'.format(user_id))
    else:
        return HttpResponse('Access Denied')

def stream(request):
    logged_in_user = request.user
    following_list = request.user.following.all()
    picturelist = []
    for publisher in following_list:
        picturelist += Photo.objects.filter(Q(owner=publisher, published ='shared') | Q(owner = publisher, published= 'public')).order_by('date_published')[:10]
        # print Photo.objects.filter(owner_id=publisher.id)
        print publisher.id
    print len(picturelist)
    for picture in picturelist:
        print picture.published
    picturelist.reverse()
    for picture in picturelist:
        owner = picture.owner
        if logged_in_user not in owner.following.all() and picture.published == 'shared':
            picturelist.remove(picture)


    template = loader.get_template('imagr/stream.html')
    print len(picturelist)
    context = RequestContext(request, {
        'picturelist': picturelist,
        'logged_in_user': logged_in_user
        })
    return HttpResponse(template.render(context))

def set_cover(request, album_id, photo_id):
    logged_in_user = request.user
    photo = Photo.objects.get(pk=photo_id)
    album = Album.objects.get(pk=album_id)
    album.cover = photo
    album.has_cover = True
    album.save()
    return HttpResponseRedirect('/imagr/album/{}'.format(album_id))
