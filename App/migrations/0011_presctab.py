# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-17 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_patient_regis_bld'),
    ]

    operations = [
        migrations.CreateModel(
            name='presctab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('docid', models.IntegerField()),
                ('prdate', models.CharField(max_length=300)),
                ('pres', models.CharField(max_length=1000)),
            ],
        ),
    ]