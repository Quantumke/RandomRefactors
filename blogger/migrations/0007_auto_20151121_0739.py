# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_post_cats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cats',
            new_name='categories',
        ),
    ]
