# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_comentario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='total_comentario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=models.TextField(verbose_name=b'Comentario'),
            preserve_default=True,
        ),
    ]
