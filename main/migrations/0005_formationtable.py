# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-09 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161109_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormationTable',
            fields=[
                ('uid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('odd', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=120)),
                ('corpus', models.TextField()),
                ('more', models.CharField(max_length=120)),
            ],
        ),
    ]
