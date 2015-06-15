# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0007_auto_20150615_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 58, 32, 456602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 58, 32, 456637, tzinfo=utc)),
        ),
    ]
