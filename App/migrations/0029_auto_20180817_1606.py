# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-17 08:06
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0028_auto_20180731_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='-_-', max_length=20, null=True, verbose_name='留言者姓名')),
                ('email', models.CharField(blank=True, default='-_-', max_length=30, null=True, verbose_name='留言者邮箱')),
                ('massage', DjangoUeditor.models.UEditorField(blank='-_-', null=True, verbose_name='留言')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='留言时间')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 17, 16, 6, 2, 654718), verbose_name='评论的时间'),
        ),
    ]
