# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0004_auto_20151121_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
