# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canlii_id', models.CharField(max_length=50)),
                ('paragraph_num', models.PositiveIntegerField()),
                ('citation_count', models.PositiveIntegerField()),
                ('sentiment_sum', models.IntegerField()),
            ],
        ),
    ]