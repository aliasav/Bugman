# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0006_auto_20150316_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(db_index=True, max_length=72, choices=[(b'functional', b'Functional'), (b'logical', b'Logical'), (b'UI', b'UI'), (b'design', b'Design'), (b'typographical', b'Typographical'), (b'system', b'System'), (b'standards', b'Standards'), (b'requirements', b'Requirements')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bug',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 18, 50, 24, 297698), auto_now_add=True),
            preserve_default=True,
        ),
    ]
