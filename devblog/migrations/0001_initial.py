# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 14:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('category', models.CharField(choices=[('CV', 'CV'), ('Serveur', 'Serveur'), ('Linux', 'Linux'), ('Divers', 'Divers')], max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]