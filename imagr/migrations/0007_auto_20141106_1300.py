# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagr', '0006_auto_20141105_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagr_user',
            name='following',
            field=models.ManyToManyField(to='imagr.Imagr_User', null=True, blank=True),
            preserve_default=True,
        ),
    ]
