# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0008_auto_20141106_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagr_user',
            name='email',
            field=models.EmailField(default='username@hotmail.com', max_length=75),
            preserve_default=False,
        ),
    ]
