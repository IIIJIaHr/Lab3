# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0006_product_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City12',
        ),
        migrations.AddField(
            model_name='recall',
            name='date_sent',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
