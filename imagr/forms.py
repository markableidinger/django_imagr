from django import forms
from models import Photo

PUBLISH_OPTIONS = (
    ('private', 'This photo is private'),
    ('public', 'This photo is publicly viewable'),
    ('shared', 'This photo is viewable by shared users'))

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=60)
	published = forms.ChoiceField(PUBLISH_OPTIONS)
	file = forms.FileField()
