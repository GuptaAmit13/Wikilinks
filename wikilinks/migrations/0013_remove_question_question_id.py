# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikilinks', '0012_myuser_current'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_id',
        ),
    ]
