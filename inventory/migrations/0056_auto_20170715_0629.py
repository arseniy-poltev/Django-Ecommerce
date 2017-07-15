# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-15 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0055_stocklocationmovement'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocklocationmovement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocklocationmovement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
