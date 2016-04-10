# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('picture', '0003_album_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('page_size', models.PositiveSmallIntegerField(help_text=b'number of pictures displayed per each page', verbose_name=b'page size')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
