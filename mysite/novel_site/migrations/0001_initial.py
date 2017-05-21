# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 00:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookTableOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=70, null=True)),
                ('content', models.TextField()),
                ('need_confirm', models.BooleanField(default=0)),
                ('book_id', models.IntegerField(null=True, verbose_name='book_id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookTableThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=70, null=True)),
                ('content', models.TextField()),
                ('need_confirm', models.BooleanField(default=0)),
                ('book_id', models.IntegerField(null=True, verbose_name='book_id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookTableTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=70, null=True)),
                ('content', models.TextField()),
                ('need_confirm', models.BooleanField(default=0)),
                ('book_id', models.IntegerField(null=True, verbose_name='book_id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InfoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, unique=True)),
                ('status', models.CharField(max_length=5, null=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('store_des', models.IntegerField(null=True, verbose_name='book_table_index')),
                ('image', models.CharField(max_length=70, null=True, verbose_name='image_des')),
                ('resume', models.CharField(max_length=300, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_boos', to='novel_site.AuthorTable', verbose_name='author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cate_books', to='novel_site.CategoryTable', verbose_name='category')),
            ],
        ),
        migrations.AddField(
            model_name='booktabletwo',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel_site.InfoTable', verbose_name='title'),
        ),
        migrations.AddField(
            model_name='booktablethree',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel_site.InfoTable', verbose_name='title'),
        ),
        migrations.AddField(
            model_name='booktableone',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel_site.InfoTable', verbose_name='title'),
        ),
    ]
