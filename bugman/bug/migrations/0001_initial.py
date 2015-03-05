# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0001_initial'),
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('description', models.TextField(max_length=600, null=True, blank=True)),
                ('link', models.URLField(max_length=300, null=True, blank=True)),
                ('screenshot', models.ImageField(null=True, upload_to=b'bugs_screenshots', blank=True)),
                ('guidelines', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 2, 28, 18, 23, 38, 672842), auto_now_add=True)),
                ('fixed_at', models.DateTimeField(null=True)),
                ('category', models.CharField(db_index=True, max_length=30, choices=[(b'functional', b'Functional'), (b'logical', b'Logical'), (b'UI', b'UI'), (b'design', b'Design'), (b'typographical', b'Typographical'), (b'system', b'System'), (b'standards', b'Standards'), (b'requirements', b'Requirements')])),
                ('status', models.CharField(db_index=True, max_length=30, choices=[(b'open', b'Open'), (b'closed', b'Closed'), (b'cancelled', b'Cancelled'), (b'deferred', b'Deferred'), (b'assigned', b'Assigned')])),
                ('priority', models.CharField(db_index=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')])),
                ('assigned_developer', models.ForeignKey(related_name='assigned_developer', to='developer.Developer')),
                ('reporter', models.ForeignKey(related_name='reporter', to='reporter.Reporter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
