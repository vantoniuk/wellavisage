# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0005_pictureconfig_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='picture',
        ),
        migrations.AddField(
            model_name='album',
            name='pictures',
            field=models.ManyToManyField(related_name='picture', to='picture.Picture'),
            preserve_default=True,
        ),
    ]
