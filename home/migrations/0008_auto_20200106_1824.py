# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-06 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200106_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
