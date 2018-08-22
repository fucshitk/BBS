# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-25 08:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_auto_20180725_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 25, 16, 59, 57, 65334), verbose_name='评论的时间'),
        ),
    ]
