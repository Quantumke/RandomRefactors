# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_auto_20151120_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=datetime.datetime(2015, 11, 21, 7, 14, 34, 183060, tzinfo=utc), unique=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 11, 21, 7, 14, 44, 517329, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
