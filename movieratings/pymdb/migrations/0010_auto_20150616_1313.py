# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pymdb.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0009_auto_20150615_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[pymdb.models.validate_movie_rating]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
