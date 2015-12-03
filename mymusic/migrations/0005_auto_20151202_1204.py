# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0004_userplaylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='language',
            field=models.CharField(max_length=20),
        ),
    ]
