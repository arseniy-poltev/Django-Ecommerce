# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0050_auto_20170711_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umbrellaproductmodel',
            name='product_type',
            field=models.CharField(blank=True, choices=[('PL', 'Blanket'), ('BA', 'Basket'), ('CA', 'Carrier'), ('JA', 'Jacket'), ('SW', 'Sweater'), ('CU', 'Cushion')], max_length=2, null=True),
        ),
    ]
