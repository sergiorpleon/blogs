# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_entrada_total_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'/photos'),
            preserve_default=True,
        ),
    ]
