# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('l1', '0002_auto_20150704_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
