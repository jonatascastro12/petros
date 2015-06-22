# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AddField(
            model_name='group',
            name='userprofiles',
            field=models.ManyToManyField(to='main.UserProfile', blank=True),
        ),
    ]
