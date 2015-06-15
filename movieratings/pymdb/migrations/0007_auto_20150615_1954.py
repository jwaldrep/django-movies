# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0006_rater_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='rater',
            name='job',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 54, 36, 104619, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='rating',
            name='time_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 19, 54, 36, 104658, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='pymdb.Genre'),
        ),
    ]
