# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-04-03 04:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_newrequest_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateofmembership',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 3, 5, 21, 14, 257328)),
        ),
    ]
