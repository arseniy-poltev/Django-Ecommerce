# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0080_auto_20170917_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='umbrellaproduct',
            name='production_remark',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='umbrellaproductmodel',
            name='umbrella_product_model',
            field=models.TextField(blank=True, null=True),
        ),
    ]
