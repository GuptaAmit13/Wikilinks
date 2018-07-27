# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0006_remove_user_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_receiptno',
            field=models.IntegerField(default=0),
        ),
    ]
