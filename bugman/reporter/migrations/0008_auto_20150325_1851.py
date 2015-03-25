# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0007_auto_20150325_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 18, 51, 17, 108075), auto_now_add=True),
            preserve_default=True,
        ),
    ]