# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0007_carouselconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselconfig',
            name='aligment',
            field=models.CharField(default='C', max_length=2, verbose_name=b'aligment', choices=[(b'C', b'Center'), (b'L', b'Left'), (b'R', b'Right')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carouselconfig',
            name='change_effect',
            field=models.CharField(default='S', max_length=4, verbose_name=b'change effect', choices=[(b'S', b'Slide'), (b'FI', b'Fade In'), (b'FO', b'Fade Out')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carouselconfig',
            name='navigation',
            field=models.CharField(default='NA', max_length=4, verbose_name=b'navigation type', choices=[(b'NA', b'None'), (b'BF', b'Back and forward'), (b'SC', b'Anchor type of navigation'), (b'SCT', b'Anchor type of navigation with text description')]),
            preserve_default=False,
        ),
    ]
