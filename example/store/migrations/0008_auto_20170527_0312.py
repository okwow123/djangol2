# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 03:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20170518_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Store', 'verbose_name_plural': 'Store'},
        ),
    ]