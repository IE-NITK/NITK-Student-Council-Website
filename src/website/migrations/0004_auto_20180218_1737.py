# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-18 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_club_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='logo',
            field=models.CharField(max_length=500),
        ),
    ]
