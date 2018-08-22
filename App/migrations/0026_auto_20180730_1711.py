# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-30 09:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_auto_20180730_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_num', models.IntegerField(blank=True, default=0, null=True, verbose_name='点赞数')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Article', verbose_name='被赞文章')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User', verbose_name='点赞用户')),
            ],
        ),
        migrations.RemoveField(
            model_name='new_likes',
            name='author',
        ),
        migrations.RemoveField(
            model_name='new_likes',
            name='content_type',
        ),
        migrations.AlterField(
            model_name='comment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 30, 17, 11, 5, 393781), verbose_name='评论的时间'),
        ),
        migrations.DeleteModel(
            name='New_Likes',
        ),
    ]
