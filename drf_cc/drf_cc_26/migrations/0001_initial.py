# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrfCc26Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abc_def', models.BooleanField(default=True)),
            ],
        ),
    ]