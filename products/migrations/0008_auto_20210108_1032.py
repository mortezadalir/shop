# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-01-08 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210108_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]