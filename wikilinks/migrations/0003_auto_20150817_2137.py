# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0002_user_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 21, 37, 19, 952157), verbose_name=b'Start Time'),
        ),
    ]
