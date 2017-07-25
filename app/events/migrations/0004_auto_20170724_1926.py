# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170724_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='facebook_event_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
