# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmanage',
            name='store_email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cmanage',
            name='user_email',
            field=models.CharField(max_length=50),
        ),
    ]
