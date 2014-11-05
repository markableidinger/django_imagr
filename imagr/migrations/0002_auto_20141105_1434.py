# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagr_user',
            old_name='USERNAME_FIELD',
            new_name='identifier',
        ),
    ]
