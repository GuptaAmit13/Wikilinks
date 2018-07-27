# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0017_auto_20150828_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 23, 21, 6, 220702, tzinfo=utc)),
        ),
    ]
