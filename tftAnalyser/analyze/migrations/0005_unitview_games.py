# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-28 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0004_unitview'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitview',
            name='games',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
