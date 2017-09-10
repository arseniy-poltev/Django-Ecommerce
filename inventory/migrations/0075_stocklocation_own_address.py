# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0019_relationaddress_default'),
        ('inventory', '0074_auto_20170909_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocklocation',
            name='own_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.OwnAddress'),
        ),
    ]
