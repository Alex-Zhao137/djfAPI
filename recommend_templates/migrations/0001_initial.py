# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 13:16
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='??????')),
                ('gender', models.CharField(choices=[('male', '???'), ('female', '???')], default='', max_length=10)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('image', models.ImageField(default='img/default.png', upload_to='image/%Y/%m')),
                ('birday', models.DateField(blank=True, null=True, verbose_name='??????')),
                ('real_name', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='????????????')),
                ('education', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='????????????')),
                ('expertise', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='????????????')),
                ('field', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='????????????')),
                ('third_party', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='???????????????')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '????????????',
                'verbose_name_plural': '????????????',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='????????????')),
                ('type', models.CharField(choices=[('jg', '??????'), ('fxyc', '????????????'), ('syjs', '????????????')], max_length=20, verbose_name='????????????')),
                ('content', models.TextField(verbose_name='??????')),
                ('page_view', models.IntegerField(default=0, verbose_name='????????????')),
                ('compliment_num', models.IntegerField(default=0, verbose_name='????????????')),
                ('collect_num', models.IntegerField(default=0, verbose_name='????????????')),
                ('status', models.CharField(choices=[('dhd', '?????????'), ('yjj', '?????????')], max_length=20, verbose_name='????????????')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='????????????')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='????????????')),
                ('exist', models.BooleanField(default=True, verbose_name='??????')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='??????id')),
            ],
            options={
                'verbose_name': '??????',
                'verbose_name_plural': '??????',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='??????')),
                ('classify', models.CharField(max_length=20, verbose_name='??????')),
                ('label', models.CharField(max_length=20, verbose_name='??????')),
                ('text', models.TextField(verbose_name='??????')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='????????????')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='????????????')),
                ('exist', models.BooleanField(default=True, verbose_name='??????')),
            ],
            options={
                'verbose_name': '??????',
                'verbose_name_plural': '??????',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[(1, '????????????'), (2, '????????????'), (3, '????????????')], max_length=10, verbose_name='????????????')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='????????????')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='????????????')),
                ('exist', models.BooleanField(default=True, verbose_name='??????')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend_templates.News', verbose_name='??????id')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='??????id')),
            ],
            options={
                'verbose_name': '????????????',
                'verbose_name_plural': '????????????',
            },
        ),
    ]
