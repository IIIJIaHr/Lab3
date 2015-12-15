# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('country', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
                ('category', models.ForeignKey(to='lab3.Category')),
                ('manufacture', models.ForeignKey(to='lab3.Manufacture')),
            ],
        ),
        migrations.CreateModel(
            name='Recall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=200)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='recalls',
            field=models.ManyToManyField(to='lab3.Recall'),
        ),
    ]
