# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-11 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_salesorder_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='paid_comission',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='paid_on_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]