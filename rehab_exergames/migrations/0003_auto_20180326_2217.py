# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-26 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehab_exergames', '0002_auto_20180321_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstraintCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='rehabilitationexergame',
            name='associated_pathologies',
            field=models.ManyToManyField(blank=True, to='pathologies.Pathology'),
        ),
        migrations.AlterField(
            model_name='rehabilitationexergame',
            name='rehabilitation_type',
            field=models.CharField(choices=[('wide_physical', 'Physical - Wide Focus'), ('tight_physical', 'Physical - Tight Focus'), ('behavioral', 'Behavioral'), ('cognitive', 'Cognitive')], max_length=20),
        ),
    ]
