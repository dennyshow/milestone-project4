# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-06 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('image', models.ImageField(upload_to='images')),
                ('details', models.CharField(max_length=255)),
                ('history', models.TextField()),
                ('quantity', models.IntegerField()),
                ('artefact', models.CharField(choices=[('HIS', 'Historical'), ('CUL', 'Cultural'), ('REL', 'Religious'), ('MED', 'Media')], max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
