# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150612_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='type',
            field=models.ForeignKey(blank=True, to='main.ChurchType', null=True),
        ),
    ]
