# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0010_auto_20150616_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('rater', 'movie')]),
        ),
    ]
