# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('imagr', '0013_remove_imagr_user_has_perm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagr_user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='imagr_user',
            name='first_name',
            field=models.CharField(default='WombatPi', max_length=30, verbose_name='first name', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagr_user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagr_user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagr_user',
            name='last_name',
            field=models.CharField(default='Machine', max_length=30, verbose_name='last name', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagr_user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagr_user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagr_user',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='email address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagr_user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagr_user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagr_user',
            name='username',
            field=models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')]),
            preserve_default=True,
        ),
    ]
