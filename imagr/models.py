from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import datetime

PUBLISH_OPTIONS = (
    ('private', 'This photo is private'),
    ('public', 'This photo is publicly viewable'),
    ('shared', 'This photo is viewable by shared users'))


class Imagr_User(AbstractBaseUser):
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)
    active = models.BooleanField(default=True)
    following = models.ManyToManyField('self', symmetrical = False, blank=True, null=True)
    following.required = False
    #following.symmetrical = False
    username = models.CharField(max_length=40, unique = True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
# class Follower(models.Model):
#     from_imagr_user_id = models.ForeignKey(Imagr_User)
#     to_imagr_user_id = models.ForeignKey(Imagr_User)


# Create your models here.
class Photo(models.Model):
    owner = models.ForeignKey(Imagr_User)
    date_uploaded = models.DateTimeField('Date Uploaded')
    date_modified = models.DateTimeField('Date Modified')
    date_published = models.DateTimeField('Date Published')
    title = models.CharField(max_length=60)
    published = models.CharField(PUBLISH_OPTIONS, max_length=7, default='private')

    def __str__(self):
        return '{} : {}'.format(self.title, self.date_modified)


class Album(models.Model):
    owner = models.ForeignKey(Imagr_User)
    date_uploaded = models.DateTimeField('Date Uploaded')
    date_modified = models.DateTimeField('Date Modified')
    date_published = models.DateTimeField('Date Published')
    title = models.CharField(max_length=60)
    published = models.CharField(PUBLISH_OPTIONS, max_length=7, default='private')
    cover = models.ForeignKey(Photo, related_name='cover', blank=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True, null=True)

    def __str__(self):
        return '{} : {}'.format(self.title, self.date_modified)

