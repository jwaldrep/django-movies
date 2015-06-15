# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0012_auto_20150615_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 43, 33, 878444, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 43, 33, 878474, tzinfo=utc)),
        ),
    ]
