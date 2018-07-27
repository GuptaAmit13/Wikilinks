# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0008_auto_20150820_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_level',
            field=models.IntegerField(default=1),
        ),
    ]
