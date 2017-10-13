# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-12 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0103_umbrellaproductmodel_customs_code_export'),
    ]

    operations = [
        migrations.AddField(
            model_name='umbrellaproduct',
            name='hs_code',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='HS Code for export.'),
        ),
    ]