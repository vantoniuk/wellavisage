# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='thumbnail',
            field=models.ForeignKey(related_name='thumbnail', default=3, to='picture.Picture'),
            preserve_default=False,
        ),
    ]
