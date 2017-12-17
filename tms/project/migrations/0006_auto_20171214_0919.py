# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='managerlevel2',
        ),
        migrations.AddField(
            model_name='media',
            name='filepath',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]