# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pymdb', '0004_auto_20150610_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='time',
        ),
    ]
