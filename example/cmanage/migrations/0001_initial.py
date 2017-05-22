# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cmanage',
            fields=[
                ('user_email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('store_email', models.CharField(max_length=50)),
                ('store_name', models.CharField(max_length=50)),
                ('store_address', models.CharField(max_length=50)),
                ('store_image', models.ImageField(upload_to=b'')),
                ('store_reward', models.IntegerField(default=0)),
                ('store_rdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]