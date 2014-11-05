# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_uploaded', models.DateTimeField(verbose_name=b'Date Uploaded')),
                ('date_modified', models.DateTimeField(verbose_name=b'Date Modified')),
                ('date_published', models.DateTimeField(verbose_name=b'Date Published')),
                ('title', models.CharField(max_length=60)),
                ('published', models.CharField(default=b'private', max_length=7, verbose_name=((b'private', b'This photo is private'), (b'public', b'This photo is publicly viewable'), (b'shared', b'This photo is viewable by shared users')))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imagr_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('active', models.BooleanField(default=True)),
                ('USERNAME_FIELD', models.CharField(unique=True, max_length=40)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_uploaded', models.DateTimeField(verbose_name=b'Date Uploaded')),
                ('date_modified', models.DateTimeField(verbose_name=b'Date Modified')),
                ('date_published', models.DateTimeField(verbose_name=b'Date Published')),
                ('title', models.CharField(max_length=60)),
                ('published', models.CharField(default=b'private', max_length=7, verbose_name=((b'private', b'This photo is private'), (b'public', b'This photo is publicly viewable'), (b'shared', b'This photo is viewable by shared users')))),
                ('owner', models.ForeignKey(to='imagr.Imagr_User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(to='imagr.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(to='imagr.Imagr_User'),
            preserve_default=True,
        ),
    ]
