# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-27 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0036_auto_20171127_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelistsetting',
            name='price_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.PriceList'),
        ),
    ]
