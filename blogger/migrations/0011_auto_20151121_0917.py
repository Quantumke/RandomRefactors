# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0010_post_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='counter',
            field=models.IntegerField(),
        ),
    ]
