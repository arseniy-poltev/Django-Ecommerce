# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0017_auto_20170909_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='business_name',
            field=models.CharField(default='tt', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='contact_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='contact_mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='contact_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownaddress',
            name='business_name',
            field=models.CharField(default='11', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ownaddress',
            name='contact_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownaddress',
            name='contact_mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownaddress',
            name='contact_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ownaddress',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='relationaddress',
            name='business_name',
            field=models.CharField(default='11', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationaddress',
            name='contact_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='relationaddress',
            name='contact_mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='relationaddress',
            name='contact_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='relationaddress',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
