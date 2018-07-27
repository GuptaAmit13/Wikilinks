# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0018_auto_20150828_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='last',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 28, 8, 10, 22, 169243, tzinfo=utc)),
        ),
    ]
