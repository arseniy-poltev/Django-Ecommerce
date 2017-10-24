# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-24 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0019_auto_20170920_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('DR', 'Draft'), ('WC', 'Waiting for confirmation'), ('WA', 'Awaiting delivery'), ('PL', 'Partially Delivered'), ('DL', 'Delivered'), ('IN', 'Invoice added')], default='DR', max_length=2),
        ),
    ]