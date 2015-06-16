# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150609_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='church_account',
            field=models.ForeignKey(editable=False, to='main.ChurchAccount'),
        ),
        migrations.AlterField(
            model_name='group',
            name='church_account',
            field=models.ForeignKey(editable=False, to='main.ChurchAccount'),
        ),
        migrations.AlterField(
            model_name='memberfunction',
            name='church_account',
            field=models.ForeignKey(editable=False, to='main.ChurchAccount'),
        ),
        migrations.AlterField(
            model_name='minute',
            name='church_account',
            field=models.ForeignKey(editable=False, to='main.ChurchAccount'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(null=True, verbose_name=b'Birth Date', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='church_account',
            field=models.ForeignKey(editable=False, to='main.ChurchAccount'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cpf',
            field=models.CharField(max_length=14, null=True, verbose_name=b'CPF', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='situation',
            field=models.CharField(default=b'A', max_length=7, verbose_name=b'Situation', choices=[(b'A', b'Active'), (b'I', b'Inactive')]),
        ),
    ]
