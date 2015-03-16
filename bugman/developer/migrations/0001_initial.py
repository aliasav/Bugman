# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import developer.models
import datetime
import django_extensions.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=200, null=True, db_index=True)),
                ('guid', django_extensions.db.fields.UUIDField(db_index=True, editable=False, blank=True)),
                ('xp', models.CharField(max_length=20, null=True)),
                ('badges', developer.models.ListField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 2, 28, 18, 23, 38, 671326), auto_now_add=True)),
                ('active_bugs', developer.models.ListField(null=True)),
                ('fixed_bugs', developer.models.ListField(null=True)),
                ('user', models.OneToOneField(related_name='developer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
