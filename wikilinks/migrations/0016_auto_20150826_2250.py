# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0015_auto_20150826_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 17, 20, 17, 870103, tzinfo=utc)),
        ),
    ]
