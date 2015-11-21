# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0007_auto_20151121_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
    ]
