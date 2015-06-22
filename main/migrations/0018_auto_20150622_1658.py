# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150622_1649'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Weekday',
        ),
        migrations.AddField(
            model_name='group',
            name='weekday',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'0', 'Segunda-feira'), (b'1', 'Ter\xe7a-feira'), (b'2', 'Quarta-feira'), (b'3', 'Quinta-feira'), (b'4', 'Sexta-feira'), (b'5', 'S\xe1bado'), (b'6', 'Domingo')]),
        ),
    ]
