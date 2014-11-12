# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0012_imagr_user_has_perm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagr_user',
            name='has_perm',
        ),
    ]
