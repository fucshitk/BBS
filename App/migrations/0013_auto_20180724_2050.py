# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-24 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_auto_20180724_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pinglun',
            field=models.CharField(default='...', max_length=255, verbose_name='评论'),
        ),
    ]
