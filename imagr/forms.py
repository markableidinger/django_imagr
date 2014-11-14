from django import forms
from models import Photo

PUBLISH_OPTIONS_PHOTO = (
    ('private', 'This photo is private'),
    ('public', 'This photo is publicly viewable'),
    ('shared', 'This photo is viewable by shared users'))

PUBLISH_OPTIONS_ALBUM = (
    ('private', 'This album is private'),
    ('public', 'This album is publicly viewable'),
    ('shared', 'This album is viewable by shared users'))

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=60)
	published = forms.ChoiceField(PUBLISH_OPTIONS_PHOTO)
	file = forms.FileField()

class CreateAlbumForm(forms.Form):
	title = forms.CharField(max_length=60)
	published = forms.ChoiceField(PUBLISH_OPTIONS_ALBUM)

class FollowerForm(forms.Form):
    username = forms.CharField(max_length=80)
