# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-05 11:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.CharField(blank=True, max_length=20, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Patients Entries',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('village', models.CharField(max_length=200)),
                ('neighborhood', models.CharField(max_length=200)),
                ('compound', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='PatientSymptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Patient Symptom',
                'verbose_name_plural': 'Patient Symptoms',
            },
        ),
        migrations.CreateModel(
            name='Refugee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(db_index=True, max_length=100, verbose_name='phone number')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('refugee_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Refugee',
                'verbose_name_plural': 'Refugees',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refugee.Location'),
        ),
        migrations.AddField(
            model_name='entry',
            name='refugee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refugee.Refugee'),
        ),
        migrations.AddField(
            model_name='entry',
            name='symptoms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refugee.PatientSymptom'),
        ),
    ]
