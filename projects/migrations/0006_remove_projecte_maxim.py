# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160602_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecte',
            name='maxim',
        ),
    ]
