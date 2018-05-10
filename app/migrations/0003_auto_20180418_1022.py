# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180418_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='entrada',
            new_name='categoria',
        ),
    ]
