# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0002_auto_20151213_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='country',
        ),
    ]
