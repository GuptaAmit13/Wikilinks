# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0009_question_question_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='question_end',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='question_start',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
