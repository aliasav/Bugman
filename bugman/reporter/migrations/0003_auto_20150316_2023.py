# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_auto_20150228_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 20, 23, 53, 909512), auto_now_add=True),
            preserve_default=True,
        ),
    ]
