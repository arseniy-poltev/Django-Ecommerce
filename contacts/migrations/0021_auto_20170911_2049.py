# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-11 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0020_relation__xero_contact_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='contact_first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownaddress',
            name='contact_first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='relation',
            name='contact_first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='relationaddress',
            name='contact_first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]