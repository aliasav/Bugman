# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0007_auto_20150325_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 18, 51, 17, 108635), auto_now_add=True),
            preserve_default=True,
        ),
    ]
