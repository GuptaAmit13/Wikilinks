# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0011_auto_20150824_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='current',
            field=models.IntegerField(default=0),
        ),
    ]
