from django.db import models
from django.contrib.auth.models import User

PUBLISH_OPTIONS = (
    ('private', 'This photo is private'),
    ('public', 'This photo is publicly viewable'),
    ('shared', 'This photo is viewable by shared users'))


class Imagr_User(models.Model):
    user = models.OneToOneField(User)
    active = models.BooleanField(default=True)
    id = models.AutoField(primary_key=True)
    # following stuff


# Create your models here.
class Photo(models.Model):
    owner = models.ForeignKey(Imagr_User)
    date_uploaded = models.DateTimeField('Date Uploaded')
    date_modified = models.DateTimeField('Date Modified')
    date_published = models.DateTimeField('Date Published')
    title = models.CharField(max_length=60)
    published = models.CharField(PUBLISH_OPTIONS, max_length=7, default='private')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return '{} : {}'.format(title, date_modified)


class Album(models.Model):
    owner = models.ForeignKey(Imagr_User)
    date_uploaded = models.DateTimeField('Date Uploaded')
    date_modified = models.DateTimeField('Date Modified')
    date_published = models.DateTimeField('Date Published')
    title = models.CharField(max_length=60)
    published = models.CharField(PUBLISH_OPTIONS, max_length=7, default='private')
    cover = models.ForeignKey(Photo)
    id = models.AutoField(primary_key=True)



