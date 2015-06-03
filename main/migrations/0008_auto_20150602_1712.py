# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150602_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='discipler',
            field=models.ForeignKey(related_name='discipler_user', verbose_name=b'Discipler', blank=True, to='main.UserProfile', null=True),
        ),
    ]
