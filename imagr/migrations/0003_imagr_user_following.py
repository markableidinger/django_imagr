# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0002_auto_20141105_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagr_user',
            name='following',
            field=models.ManyToManyField(related_name='following_rel_+', to='imagr.Imagr_User'),
            preserve_default=True,
        ),
    ]
