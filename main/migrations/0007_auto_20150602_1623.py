# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150602_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='discipler',
            field=models.ForeignKey(related_name='discipler_user', to='main.UserProfile'),
        ),
    ]
