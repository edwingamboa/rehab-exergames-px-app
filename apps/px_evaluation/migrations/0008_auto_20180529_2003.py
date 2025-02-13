# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('px_evaluation', '0007_auto_20180516_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pxevaluation',
            name='current_stage',
            field=models.CharField(choices=[('rehab_env_analysis', 'Rehabilitation Environment Analysis'), ('eval_goal_def', 'Evaluation Goal Definition'), ('aspects_sel', 'Evaluation Aspects Selection'), ('methods_sel', 'Evaluation Methods Selection'), ('instruments_sel', 'Evaluation Instruments Selection'), ('eval_prep', 'Evaluation Preparation'), ('report', 'Results Analysis and Reporting')], default='rehab_env_analysis', max_length=20),
        ),
    ]
