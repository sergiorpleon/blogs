# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180418_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='contenido',
            field=models.TextField(max_length=300, verbose_name=b'Comentario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
