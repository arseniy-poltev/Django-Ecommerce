# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-24 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0032_auto_20170624_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='quantity_in_stock',
        ),
    ]
