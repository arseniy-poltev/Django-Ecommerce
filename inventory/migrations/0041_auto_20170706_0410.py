# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0040_auto_20170706_0356'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModelProductionDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Step name')),
                ('description', models.TextField(verbose_name='What to do and how to do it')),
                ('image', models.FileField(upload_to='media/product_models/production_description/images/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='productmodelimage',
            name='image',
            field=models.FileField(upload_to='media/product_model/images/%Y/%m/%d'),
        ),
    ]
