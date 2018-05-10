# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_entrada_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'photos/', blank=True),
            preserve_default=True,
        ),
    ]
