# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-25 12:12
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('vicinity', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TestDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('icon', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]