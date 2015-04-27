# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rdfserializer', '0001_auto_20150316_2020'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='fieldrelation',
            table='fieldsrelations',
        ),
        migrations.AlterModelTable(
            name='namespace',
            table='namespaces',
        ),
        migrations.AlterModelTable(
            name='node',
            table='nodes',
        ),
        migrations.AlterModelTable(
            name='scheme',
            table='schemes',
        ),
    ]
