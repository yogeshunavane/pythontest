# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-08-23 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='test',
            field=models.CharField(default=123, max_length=1000),
            preserve_default=False,
        ),
    ]