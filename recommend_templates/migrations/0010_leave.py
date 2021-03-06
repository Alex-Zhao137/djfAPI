# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-29 22:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_templates', '0009_auto_20181029_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='留言')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend_templates.Forum', verbose_name='帖子')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
            },
        ),
    ]
