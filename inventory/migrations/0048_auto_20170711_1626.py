# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0047_auto_20170711_1621'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductPattern',
            new_name='ProductModelPattern',
        ),
        migrations.RenameField(
            model_name='umbrellaproductbillofmaterial',
            old_name='umbrella_product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='umbrellaproductimage',
            old_name='umbrella_product',
            new_name='product',
        ),
    ]