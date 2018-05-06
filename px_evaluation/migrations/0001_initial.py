# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resources', '0002_auto_20180506_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True)),
                ('resources', models.ManyToManyField(blank=True, to='resources.Resource')),
            ],
        ),
    ]