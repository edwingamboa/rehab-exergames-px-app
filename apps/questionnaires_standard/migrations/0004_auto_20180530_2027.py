# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires_standard', '0003_auto_20180529_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='type',
            field=models.CharField(choices=[('validity', 'Validity'), ('reliability', 'Reliability')], max_length=20),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='pre_testing_report',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_pre_test_report', to='resources.Resource'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='status',
            field=models.CharField(choices=[('init', 'Initiated'), ('in_design', 'In Design'), ('in_pre_test', 'In Pre-Testing'), ('finished', 'Finished'), ('in_review', 'In Review')], default='init', max_length=20),
        ),
    ]