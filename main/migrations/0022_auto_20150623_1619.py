# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_chuchaccountsettings_userpreferences'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpreferences',
            options={'verbose_name': 'User Preference'},
        ),
        migrations.AlterField(
            model_name='group',
            name='weekday',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'0', b'Monday'), (b'1', b'Tuesday'), (b'2', b'Wednesday'), (b'3', b'Thursday'), (b'4', b'Friday'), (b'5', b'Saturday'), (b'6', b'Sunday')]),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='language',
            field=models.CharField(default=b'pt-br', max_length=10, choices=[(b'pt-br', b'Portugu\xc3\xaas'), (b'en-us', b'English')]),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='user',
            field=models.OneToOneField(related_name='preferences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='has_child',
            field=models.CharField(blank=True, max_length=b'1', null=True, verbose_name=b'Has Child?', choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
    ]
