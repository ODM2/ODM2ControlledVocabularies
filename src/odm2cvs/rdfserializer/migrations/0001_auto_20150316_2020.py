# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rdfserializer', 'data_migration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scheme',
            options={'ordering': ['-name']},
        ),
    ]
