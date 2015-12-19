# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0007_auto_20151216_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recall',
            name='date_sent',
        ),
    ]
