# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0008_auto_20150615_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 41, 20, 646721, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 41, 20, 646758, tzinfo=utc)),
        ),
    ]
