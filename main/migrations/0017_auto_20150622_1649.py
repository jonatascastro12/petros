# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150622_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_name', models.CharField(max_length=50)),
                ('day_name_abrev', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='address',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='type',
            field=models.CharField(max_length=20, choices=[(b'cell', b'Cell'), (b'department', b'Department'), (b'ministry', b'Ministry')]),
        ),
    ]
