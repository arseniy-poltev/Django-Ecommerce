# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0051_auto_20170711_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='umbrellaproduct',
            options={'ordering': ('collection', 'umbrella_product_model__number', 'colour')},
        ),
        migrations.AddField(
            model_name='productbillofmaterial',
            name='use_default_qty',
            field=models.BooleanField(default=True, verbose_name='Use parent/umbrella qty value'),
        ),
    ]
