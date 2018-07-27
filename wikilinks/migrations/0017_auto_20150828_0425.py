# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0016_auto_20150826_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_receiptno',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 22, 55, 44, 800931, tzinfo=utc)),
        ),
    ]
