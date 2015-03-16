# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0003_auto_20150316_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 20, 24, 14, 632873), auto_now_add=True),
            preserve_default=True,
        ),
    ]