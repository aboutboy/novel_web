# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel_site', '0006_categorytable_cate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel_site.CategoryTable', verbose_name='cate'),
        ),
    ]
