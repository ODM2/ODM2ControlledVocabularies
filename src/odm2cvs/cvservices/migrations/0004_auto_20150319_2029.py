# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvservices', '0003_auto_20150319_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actiontype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Action Type'},
        ),
    ]
