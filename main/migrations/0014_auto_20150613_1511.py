# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150613_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='how_many_child',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
    ]
