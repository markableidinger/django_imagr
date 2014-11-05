# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0004_auto_20141105_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagr_user',
            old_name='identifier',
            new_name='username',
        ),
    ]
