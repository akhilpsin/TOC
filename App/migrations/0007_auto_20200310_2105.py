# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-10 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_out_lab_regis_out_pharmacy_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='out_lab_regis',
            name='password',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='out_lab_regis',
            name='username',
            field=models.CharField(default='none', max_length=30),
        ),
    ]