# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imbdb_url',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video_date',
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=255),
        ),
    ]
