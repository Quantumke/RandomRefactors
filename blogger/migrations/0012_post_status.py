# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0011_auto_20151121_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default=datetime.datetime(2015, 11, 21, 10, 33, 7, 339024, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
