# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 14:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryWebApp', '0002_remove_entry_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='date',
        ),
        migrations.AddField(
            model_name='entry',
            name='dateTime',
            field=models.DateTimeField(default=datetime.date(2016, 12, 19)),
            preserve_default=False,
        ),
    ]
