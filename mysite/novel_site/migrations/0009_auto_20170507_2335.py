# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel_site', '0008_auto_20170507_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cate_books', to='novel_site.CategoryTable', verbose_name='category'),
        ),
    ]
