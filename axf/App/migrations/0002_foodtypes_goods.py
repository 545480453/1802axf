# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-13 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=100)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=120)),
                ('typesort', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=100)),
                ('productimg', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=100)),
                ('isxf', models.IntegerField()),
                ('pmdesc', models.IntegerField()),
                ('specifics', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('marketprice', models.CharField(max_length=100)),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=100)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]
