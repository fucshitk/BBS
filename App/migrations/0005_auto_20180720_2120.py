# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-20 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20180720_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uicon',
            field=models.ImageField(default='https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2475094404,2581596256&fm=27&gp=0.jpg', upload_to='uploads/uicon/', verbose_name='头像'),
        ),
    ]