# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0013_remove_question_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 22, 34, 41, 928987)),
        ),
        migrations.AddField(
            model_name='myuser',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 22, 34, 41, 928947)),
        ),
    ]
