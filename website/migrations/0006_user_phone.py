# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='SOME STRING', max_length=25),
        ),
    ]
