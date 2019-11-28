# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-27 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191127_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='artefact',
            field=models.CharField(choices=[('HIS', 'Historical'), ('CUL', 'Cultural'), ('REL', 'Religious'), ('MED', 'Media')], max_length=3),
        ),
    ]
