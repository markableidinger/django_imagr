# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0011_imagr_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagr_user',
            name='has_perm',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
