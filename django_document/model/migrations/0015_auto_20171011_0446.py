# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0014_place_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='serves_hot_dogs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='serves_pizza',
            field=models.BooleanField(default=False),
        ),
    ]
