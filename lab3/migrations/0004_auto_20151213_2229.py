# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0003_remove_product_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='recalls',
        ),
        migrations.AddField(
            model_name='recall',
            name='product_id',
            field=models.ForeignKey(default=1, to='lab3.Product'),
            preserve_default=False,
        ),
    ]
