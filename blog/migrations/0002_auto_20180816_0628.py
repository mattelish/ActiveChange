# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-16 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='blog',
            new_name='post',
        ),
    ]
