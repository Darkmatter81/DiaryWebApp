# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryWebApp', '0007_auto_20161221_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='lastUpdated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]