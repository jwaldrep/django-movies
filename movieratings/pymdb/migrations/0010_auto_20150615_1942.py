# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0009_auto_20150615_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='job',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 42, 30, 905403, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 42, 30, 905438, tzinfo=utc)),
        ),
    ]
