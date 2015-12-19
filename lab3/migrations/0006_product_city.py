# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0005_city_city12'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.ForeignKey(default=1, to='lab3.City'),
            preserve_default=False,
        ),
    ]
