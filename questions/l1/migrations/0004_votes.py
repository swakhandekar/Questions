# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('l1', '0003_student_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ques', models.ForeignKey(to='l1.Question')),
                ('te', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
