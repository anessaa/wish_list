# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishList_app', '0002_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='name',
        ),
    ]