# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180418_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='total_comentario',
        ),
    ]
