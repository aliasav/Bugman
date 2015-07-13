# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0008_auto_20150325_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
