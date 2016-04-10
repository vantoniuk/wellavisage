# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('picture', '0006_auto_20151024_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=100, verbose_name=b'carousel name')),
                ('height', models.PositiveSmallIntegerField(help_text=b'images height')),
                ('width', models.PositiveSmallIntegerField(help_text=b'images width')),
                ('interval', models.PositiveSmallIntegerField(help_text=b'change interval in seconds')),
                ('pictures_only', models.BooleanField(default=True, help_text=b'display only pictures without description', verbose_name=b'pictures only')),
                ('album', models.ForeignKey(related_name='carousel_album', to='picture.Album')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
