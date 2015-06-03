# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import crop_image.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150601_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(verbose_name=b'Birth Date'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=crop_image.forms.CropImageModelField(null=True, upload_to=b'user_photos', blank=True),
        ),
    ]
