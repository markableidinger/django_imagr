# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0007_auto_20141106_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(related_name='cover', blank=True, to='imagr.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(to='imagr.Photo', null=True, blank=True),
            preserve_default=True,
        ),
    ]
