from django.contrib import admin
from imagr.models import Imagr_User, Photo, Album
# Register your models here.
admin.site.register(Imagr_User)
admin.site.register(Photo)
admin.site.register(Album)
