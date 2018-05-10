# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180418_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='total_comentario',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
