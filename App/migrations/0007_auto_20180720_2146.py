# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-20 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20180720_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uicon',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='uicon/', verbose_name='头像'),
        ),
    ]
