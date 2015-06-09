# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tinymce.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150608_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='minute',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 9, 12, 17, 17, 582000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='minute',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
