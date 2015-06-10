# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0003_auto_20150610_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(max_length=255),
        ),
    ]
