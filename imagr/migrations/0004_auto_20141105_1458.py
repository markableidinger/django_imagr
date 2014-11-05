# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0003_imagr_user_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagr_user',
            name='following',
            field=models.ManyToManyField(to='imagr.Imagr_User'),
            preserve_default=True,
        ),
    ]
