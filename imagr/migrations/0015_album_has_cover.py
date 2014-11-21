# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0014_auto_20141112_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='has_cover',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
