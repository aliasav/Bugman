# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0004_auto_20150316_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 20, 24, 33, 200423), auto_now_add=True),
            preserve_default=True,
        ),
    ]
