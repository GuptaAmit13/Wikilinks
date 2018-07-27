# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 14, 18, 23, 499094), verbose_name=b'Start Time'),
        ),
    ]
