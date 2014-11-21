from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

PUBLISH_OPTIONS = (
    ('private', 'This photo is private'),
    ('public', 'This photo is publicly viewable'),
    ('shared', 'This photo is viewable by shared users'))

# class Imagr_User_Manager(BaseUserManager):
#     def create_user(self, email, password, username):
#         if not username:
#             raise ValueError('Must provide a username')
#         if not email:
#             raise ValueError('Must provide an email')
#         user = self.model(
#             email = self.normalize_email(email),
#             username = username
#             )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, password, username):
#         if not username:
#             raise ValueError('Must provide a username')
#         # if not email:
#         #     raise ValueError('Must provide an email')
#         user = self.model(
#             # email = self.normalize_email(email),
#             username=username
#             )
#         user.is_admin = True
#         user.is_staff = True
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

class Imagr_User(AbstractUser):
    # date_joined = models.DateTimeField('Date Joined', auto_now_add=True)
    # is_active = models.BooleanField(default=True)
    following = models.ManyToManyField('self', symmetrical = False, blank=True, null=True)
    following.required = False
    # email = models.EmailField()
    # username = models.CharField(max_length=40, unique = True)
    
    # USERNAME_FIELD = 'username'
    
    # is_staff = models.BooleanField(default=False)
    
    # objects = Imagr_User_Manager()

    def __str__(self):
        return self.username
    # def get_short_name(self, name):
    #     return self.username
    # def get_full_name(self, name):
    #     return self.username
    # def has_perm(self, name):
    #     return True
    # def has_module_perms(self, name):
    #     return True

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
    has_cover = models.BooleanField(default = False)
    title = models.CharField(max_length=60)
    published = models.CharField(PUBLISH_OPTIONS, max_length=7, default='private')
    cover = models.ForeignKey(Photo, related_name='cover', blank=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True, null=True)

    def __str__(self):
        return '{} : {}'.format(self.title, self.date_modified)


