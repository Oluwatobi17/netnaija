# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-24 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190324_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='accno',
            field=models.CharField(max_length=20),
        ),
    ]
