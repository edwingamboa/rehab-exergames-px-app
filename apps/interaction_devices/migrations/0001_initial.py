# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceTechnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InteractionDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('type', models.PositiveIntegerField(choices=[(1, 'Input'), (2, 'Output'), (3, 'Input/Output')])),
                ('device_technology', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interaction_devices.DeviceTechnology')),
            ],
        ),
    ]
