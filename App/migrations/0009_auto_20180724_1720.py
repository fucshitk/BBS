# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-24 09:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20180720_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间'),
        ),
    ]