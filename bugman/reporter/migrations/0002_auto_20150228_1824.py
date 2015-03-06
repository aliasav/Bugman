# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 28, 18, 24, 15, 366765), auto_now_add=True),
            preserve_default=True,
        ),
    ]
