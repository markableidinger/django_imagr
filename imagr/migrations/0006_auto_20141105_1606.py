# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0005_auto_20141105_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(to='imagr.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagr_user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 6, 0, 6, 11, 449943, tzinfo=utc), verbose_name=b'Date Joined', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(related_name='cover', to='imagr.Photo'),
            preserve_default=True,
        ),
    ]
