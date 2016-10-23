# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 12:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(db_index=True, default='', max_length=4, unique=True)),
                ('name', models.CharField(default='', max_length=16)),
                ('since', models.DateField(default=datetime.date.today)),
                ('revenue', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
