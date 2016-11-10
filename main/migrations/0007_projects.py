# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20161109_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('uid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('corpus', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('tags', models.CharField(max_length=200)),
                ('docs', models.CharField(max_length=4000)),
            ],
        ),
    ]
