# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishList_app', '0004_item_on_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='on_list',
        ),
    ]
