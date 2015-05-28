# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.br.models
import crop_image.forms
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Church',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('cnpj', models.CharField(max_length=20, verbose_name=b'CNPJ', blank=True)),
                ('email', models.EmailField(max_length=b'200', null=True, blank=True)),
                ('address_line', models.CharField(blank=True, max_length=b'300', null=True, verbose_name=b'Endere\xc3\xa7o', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9,\\.\\s]+$", 'Special char not permitted.')])),
                ('neighborhood', models.CharField(blank=True, max_length=b'200', null=True, verbose_name=b'Bairro', validators=[django.core.validators.RegexValidator("^['a-zA-Z0-9\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd1\\s]+$", 'Special char not permitted.')])),
                ('city', models.CharField(blank=True, max_length=b'200', null=True, verbose_name=b'Cidade', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9\\s]+$", 'Special char not permitted.')])),
                ('state', models.CharField(blank=True, max_length=b'2', null=True, verbose_name=b'UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('phone1', models.CharField(max_length=15, verbose_name=b'Phone 1', blank=True)),
                ('phone2', models.CharField(max_length=15, verbose_name=b'Phone 2', blank=True)),
                ('is_mother', models.BooleanField(default=True)),
                ('logo', crop_image.forms.CropImageModelField(url=b'', null=True, upload_to=b'church_logos', blank=True)),
            ],
            options={
                'verbose_name': 'Church',
            },
        ),
        migrations.CreateModel(
            name='ChurchAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('cnpj', models.CharField(max_length=20, verbose_name=b'CNPJ', blank=True)),
                ('email', models.EmailField(max_length=b'200', null=True, blank=True)),
                ('address_line', models.CharField(blank=True, max_length=b'300', null=True, verbose_name=b'Endere\xc3\xa7o', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9,\\.\\s]+$", 'Special char not permitted.')])),
                ('neighborhood', models.CharField(blank=True, max_length=b'200', null=True, verbose_name=b'Bairro', validators=[django.core.validators.RegexValidator("^['a-zA-Z0-9\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd1\\s]+$", 'Special char not permitted.')])),
                ('city', models.CharField(blank=True, max_length=b'200', null=True, verbose_name=b'Cidade', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9\\s]+$", 'Special char not permitted.')])),
                ('state', models.CharField(blank=True, max_length=b'2', null=True, verbose_name=b'UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('phone1', models.CharField(max_length=15, verbose_name=b'Phone 1', blank=True)),
                ('phone2', models.CharField(max_length=15, verbose_name=b'Phone 2', blank=True)),
                ('logo', crop_image.forms.CropImageModelField(url=b'', null=True, upload_to=b'church_logos', blank=True)),
                ('user_admin', models.ForeignKey(related_name='church_user_admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Church Account',
            },
        ),
        migrations.CreateModel(
            name='ChurchType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Church Type',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100, choices=[(b'C', b'Cell'), (b'D', b'Department'), (b'M', b'Ministry')])),
                ('church_account', models.ForeignKey(to='main.ChurchAccount')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('previous_church', models.CharField(max_length=b'255', null=True, verbose_name=b'Previous church', blank=True)),
                ('previous_function', models.CharField(max_length=b'255', null=True, verbose_name=b'Previous function', blank=True)),
                ('baptism_date', models.DateField(verbose_name=b'Baptism date')),
                ('baptism_place', models.CharField(max_length=b'255', null=True, verbose_name=b'Baptism place', blank=True)),
                ('admission_date', models.DateField(null=True, verbose_name=b'Admission date', blank=True)),
                ('situation', models.CharField(max_length=7, verbose_name=b'Situation', choices=[(b'A', b'Active'), (b'I', b'Inactive')])),
                ('church', models.ForeignKey(to='main.Church')),
                ('church_account', models.ForeignKey(to='main.ChurchAccount')),
            ],
            options={
                'verbose_name': 'Member',
            },
        ),
        migrations.CreateModel(
            name='MemberFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text=b'Ex: Dc', max_length=60, verbose_name=b'T\xc3\xadtulo abrev.')),
                ('name', models.CharField(help_text=b'Ex: Di\xc3\xa1cono', max_length=255, verbose_name=b'T\xc3\xadtulo')),
                ('title_female', models.CharField(help_text=b'Ex: Dc\xc2\xaa', max_length=60, verbose_name=b'T\xc3\xadtulo abrev. Feminino')),
                ('name_female', models.CharField(help_text=b'Ex: Diaconisa', max_length=255, verbose_name=b'T\xc3\xadtulo Feminino')),
                ('church_account', models.ForeignKey(to='main.ChurchAccount')),
            ],
            options={
                'verbose_name': 'Fun\xe7\xe3o de membro',
                'verbose_name_plural': 'Fun\xe7\xf5es de membro',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('photo', crop_image.forms.CropImageModelField(url=b'', upload_to=b'user_photos')),
                ('type', models.CharField(max_length=100, choices=[(b'G', b'Gathered'), (b'M', b'Member')])),
                ('cpf', models.CharField(max_length=14, verbose_name=b'CPF')),
                ('rg', models.CharField(max_length=14, null=True, verbose_name=b'RG', blank=True)),
                ('birth_date', models.DateField(verbose_name=b'Data de Nascimento')),
                ('gender', models.CharField(max_length=b'1', verbose_name=b'Gender', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('blood_type', models.CharField(blank=True, max_length=b'2', null=True, verbose_name=b'Blood Type', choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'O+', b'O+'), (b'O-', b'O-')])),
                ('address_line', models.CharField(blank=True, max_length=b'300', verbose_name=b'Address', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9,\\.\\s]+$", 'Special char not permitted.')])),
                ('neighborhood', models.CharField(blank=True, max_length=b'200', verbose_name=b'Neighborhood', validators=[django.core.validators.RegexValidator("^['a-zA-Z0-9\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd1\\s]+$", 'Special char not permitted.')])),
                ('city', models.CharField(blank=True, max_length=b'200', verbose_name=b'City', validators=[django.core.validators.RegexValidator("^['a-zA-Z\xe1\xe0\xe2\xe3\xe9\xe8\xea\xed\xef\xf3\xf4\xf5\xf6\xfa\xe7\xf1\xc1\xc0\xc2\xc3\xc9\xc8\xcd\xcf\xd3\xd4\xd5\xd6\xda\xc7\xd10-9\\s]+$", 'Special char not permitted.')])),
                ('state', localflavor.br.models.BRStateField(max_length=2, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('zipcode', models.CharField(max_length=b'10', null=True, blank=True)),
                ('phone1', models.CharField(max_length=b'15', verbose_name=b'Telefone 1', blank=True)),
                ('phone2', models.CharField(max_length=b'15', verbose_name=b'Telefone 2', blank=True)),
                ('profession', models.CharField(max_length=b'200', null=True, verbose_name=b'Profession', blank=True)),
                ('work_place', models.CharField(max_length=b'200', null=True, verbose_name=b'Work place', blank=True)),
                ('father_name', models.CharField(max_length=b'255', null=True, verbose_name=b'Father name', blank=True)),
                ('mother_name', models.CharField(max_length=b'255', null=True, verbose_name=b'Mother name', blank=True)),
                ('marital_status', models.CharField(blank=True, max_length=b'1', null=True, choices=[(b'S', b'Single'), (b'D', b'Divorced'), (b'M', b'Married'), (b'W', b'Widow')])),
                ('spouse', models.CharField(max_length=b'255', null=True, verbose_name=b'Spouse', blank=True)),
                ('has_child', models.CharField(blank=True, max_length=b'1', null=True, verbose_name=b'Has Child?', choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('how_many_child', models.PositiveSmallIntegerField(default=0)),
                ('church_account', models.ForeignKey(to='main.ChurchAccount')),
                ('discipler', models.ForeignKey(related_name='discipler_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='member',
            name='member_function',
            field=models.ForeignKey(verbose_name=b'Member Function', to='main.MemberFunction'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(related_name='member', verbose_name=b'User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='church',
            name='church_account',
            field=models.ForeignKey(to='main.ChurchAccount'),
        ),
        migrations.AddField(
            model_name='church',
            name='church_mother',
            field=models.ForeignKey(related_name='mother', blank=True, to='main.Church', null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='type',
            field=models.ForeignKey(to='main.ChurchType'),
        ),
    ]
