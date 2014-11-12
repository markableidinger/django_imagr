# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0009_imagr_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagr_user',
            old_name='active',
            new_name='is_active',
        ),
    ]
