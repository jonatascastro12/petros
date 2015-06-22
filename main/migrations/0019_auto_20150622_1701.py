# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150622_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='address',
            new_name='place',
        ),
    ]
