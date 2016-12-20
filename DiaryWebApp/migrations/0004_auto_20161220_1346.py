# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 13:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryWebApp', '0003_auto_20161219_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='dateTime',
            new_name='date',
        ),
        migrations.AddField(
            model_name='entry',
            name='time',
            field=models.TimeField(default=datetime.time(13, 46, 31, 282840)),
            preserve_default=False,
        ),
    ]