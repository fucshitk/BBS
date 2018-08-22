# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-27 11:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0021_auto_20180726_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_num',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='', validators=['点', '赞', '数']),
        ),
        migrations.AddField(
            model_name='user',
            name='bgimg',
            field=models.ImageField(blank=True, default='bgimg/welcome.gif', null=True, upload_to='bgimg/', verbose_name='主页背景图片'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 27, 19, 21, 12, 543002), verbose_name='评论的时间'),
        ),
    ]