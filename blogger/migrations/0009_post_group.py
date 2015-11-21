# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0008_remove_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.CharField(default=datetime.datetime(2015, 11, 21, 7, 53, 9, 529812, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
