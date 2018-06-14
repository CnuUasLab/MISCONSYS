# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-14 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20180507_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='alphanumeric_color',
            field=models.CharField(choices=[('r', 'Red'), ('b', 'Blue'), ('g', 'Green'), ('y', 'Yellow'), ('p', 'Purple'), ('o', 'Orange')], default='r', max_length=10),
        ),
        migrations.AddField(
            model_name='target',
            name='shape_choices',
            field=models.CharField(choices=[('Ci', 'Circle'), ('St', 'Star'), ('Sq', 'Square'), ('Sc', 'Semicircle'), ('Tr', 'Triangle')], default='Ci', max_length=10),
        ),
        migrations.AddField(
            model_name='target',
            name='shape_color',
            field=models.CharField(choices=[('r', 'Red'), ('b', 'Blue'), ('g', 'Green'), ('y', 'Yellow'), ('p', 'Purple'), ('o', 'Orange')], default='r', max_length=10),
        ),
    ]
