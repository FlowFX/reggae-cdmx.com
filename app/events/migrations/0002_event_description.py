# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
