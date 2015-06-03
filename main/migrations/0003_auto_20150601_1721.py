# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150528_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(related_name='member', verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='has_child',
            field=models.CharField(blank=True, max_length=b'1', null=True, verbose_name=b'Has Child?', choices=[(b'Y', 'Sim'), (b'N', 'N\xe3o')]),
        ),
    ]
