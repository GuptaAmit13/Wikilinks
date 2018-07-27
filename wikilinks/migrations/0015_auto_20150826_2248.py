# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0014_auto_20150826_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
