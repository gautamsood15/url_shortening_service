# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-02-04 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20200127_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortener',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
