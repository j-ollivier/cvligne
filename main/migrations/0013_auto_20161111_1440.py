# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-11 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20161111_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='formationtable',
            name='link',
            field=models.CharField(blank=True, default='-', max_length=120),
        ),
        migrations.AlterField(
            model_name='formationtable',
            name='more',
            field=models.CharField(blank=True, default='-', max_length=120),
        ),
    ]
