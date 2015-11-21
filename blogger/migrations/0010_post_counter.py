# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0009_post_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='counter',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
