# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'album name')),
                ('description', models.TextField(verbose_name=b'album description', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('picture', models.ManyToManyField(to='picture.Picture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
