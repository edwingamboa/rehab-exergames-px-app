# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires_standard', '0002_measure_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='type',
            field=models.CharField(choices=[(('validity',), 'Validity'), (('reliability',), 'Reliability')], max_length=20),
        ),
    ]
