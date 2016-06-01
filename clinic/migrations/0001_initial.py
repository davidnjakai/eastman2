# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patid', models.AutoField(primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=45)),
                ('firstname', models.CharField(max_length=45)),
                ('middlename', models.CharField(blank=True, max_length=45, null=True)),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('mobilenumber', models.CharField(blank=True, max_length=45, null=True)),
                ('mobilenumber2', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('guarantor', models.IntegerField()),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('filenumber', models.IntegerField()),
                ('photolocation', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('position', models.CharField(blank=True, max_length=10, null=True)),
                ('dueamount', models.IntegerField()),
                ('insuranceamount', models.IntegerField()),
                ('balancedue', models.IntegerField()),
                ('occupation', models.CharField(blank=True, max_length=45, null=True)),
                ('employer_school', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'patients',
            },
        ),
    ]
