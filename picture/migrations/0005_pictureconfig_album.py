# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0004_pictureconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictureconfig',
            name='album',
            field=models.ForeignKey(related_name='album', default=1, to='picture.Album'),
            preserve_default=False,
        ),
    ]
