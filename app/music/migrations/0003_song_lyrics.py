# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170411_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True),
        ),
    ]
