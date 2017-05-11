# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel_site', '0007_auto_20170507_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authortable',
            name='author',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='booktableone',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel_site.InfoTable', to_field='title', verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='booktablethree',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel_site.InfoTable', to_field='title', verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='booktabletwo',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel_site.InfoTable', to_field='title', verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='categorytable',
            name='cate',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='infotable',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_boos', to='novel_site.AuthorTable', to_field='author', verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='infotable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cate_books', to='novel_site.CategoryTable', to_field='cate', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='infotable',
            name='title',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]
