# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-04-03 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20190403_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateofmembership',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
