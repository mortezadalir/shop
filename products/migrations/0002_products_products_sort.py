# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-12-27 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='products_sort',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='prod_Sort', to='products.ProductSort'),
            preserve_default=False,
        ),
    ]
