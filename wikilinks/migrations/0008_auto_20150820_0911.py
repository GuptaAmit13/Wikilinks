# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0007_user_user_receiptno'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_status',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='attempt_no',
            field=models.IntegerField(default=0),
        ),
    ]
