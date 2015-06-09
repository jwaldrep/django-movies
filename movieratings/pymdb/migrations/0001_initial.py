# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('video_date', models.DateField()),
                ('imbdb_url', models.URLField()),
                ('genre', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=64)),
                ('zip_code', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('time', models.DateTimeField()),
                ('movie', models.ForeignKey(to='pymdb.Movie')),
                ('user', models.ForeignKey(to='pymdb.Rater')),
            ],
        ),
    ]
