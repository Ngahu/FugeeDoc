# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='phone number'),
        ),
    ]
