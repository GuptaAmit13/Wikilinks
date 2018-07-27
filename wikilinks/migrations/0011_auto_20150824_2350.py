# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wikilinks', '0010_auto_20150823_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(default=1)),
                ('user_receiptno', models.IntegerField(default=0)),
                ('user_status', models.CharField(default=b'', max_length=10)),
                ('attempt_no', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
