# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0005_auto_20150818_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='start_time',
        ),
    ]
