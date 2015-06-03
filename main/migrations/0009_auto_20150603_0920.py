# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150602_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='church',
        ),
        migrations.RemoveField(
            model_name='member',
            name='church_account',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_function',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='admission_date',
            field=models.DateField(null=True, verbose_name=b'Admission date', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='baptism_date',
            field=models.DateField(null=True, verbose_name=b'Baptism date', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='baptism_place',
            field=models.CharField(max_length=b'255', null=True, verbose_name=b'Baptism place', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='church',
            field=models.ForeignKey(default=1, to='main.Church'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='member_function',
            field=models.ForeignKey(verbose_name=b'Member Function', blank=True, to='main.MemberFunction', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previous_church',
            field=models.CharField(max_length=b'255', null=True, verbose_name=b'Previous church', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previous_function',
            field=models.CharField(max_length=b'255', null=True, verbose_name=b'Previous function', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='situation',
            field=models.CharField(default='A', max_length=7, verbose_name=b'Situation', choices=[(b'A', b'Active'), (b'I', b'Inactive')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='member', verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
