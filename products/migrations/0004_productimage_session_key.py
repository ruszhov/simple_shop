# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170727_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
