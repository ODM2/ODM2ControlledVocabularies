# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldRelation',
            fields=[
                ('field_id', models.AutoField(serialize=False, primary_key=True, db_column=b'fieldId')),
                ('field_name', models.CharField(max_length=255, db_column=b'fieldName')),
            ],
            options={
                'db_table': 'FieldsRelations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('alias', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('reference', models.URLField(max_length=255)),
            ],
            options={
                'db_table': 'Namespaces',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('node_id', models.AutoField(serialize=False, primary_key=True, db_column=b'nodeId')),
                ('name', models.CharField(max_length=255)),
                ('namespace', models.ForeignKey(to='rdfserializer.Namespace')),
            ],
            options={
                'db_table': 'Nodes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('name', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('creator', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('uri', models.URLField()),
            ],
            options={
                'db_table': 'Schemes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fieldrelation',
            name='node',
            field=models.ForeignKey(to='rdfserializer.Node', db_column=b'nodeId'),
            preserve_default=True,
        ),
    ]
