# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_templates', '0002_auto_20180527_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.CharField(default='', max_length=50, verbose_name='文章url链接'),
        ),
    ]
