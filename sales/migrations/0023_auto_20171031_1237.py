# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-31 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0022_auto_20171031_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricetransport',
            old_name='from_price',
            new_name='order_from_price',
        ),
        migrations.AddField(
            model_name='pricetransport',
            name='shipping_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]