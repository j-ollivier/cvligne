# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-09 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161109_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exptable',
            name='odd',
            field=models.CharField(max_length=20),
        ),
    ]
