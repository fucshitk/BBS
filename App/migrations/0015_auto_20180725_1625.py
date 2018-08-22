# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-25 08:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pinglun',
        ),
        migrations.AlterField(
            model_name='comment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 25, 16, 25, 41, 535923), verbose_name='评论的时间'),
        ),
    ]