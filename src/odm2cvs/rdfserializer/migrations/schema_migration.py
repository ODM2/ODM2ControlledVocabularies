# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldRelation',
            fields=[
                ('field_id', models.AutoField(serialize=False, primary_key=True, db_column='fieldId')),
                ('field_name', models.CharField(max_length=255, db_column='fieldName')),
            ],
            options={
                'db_table': 'fieldsrelations',
            },
        ),
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('alias', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('reference', models.URLField(max_length=255)),
            ],
            options={
                'db_table': 'namespaces',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('node_id', models.AutoField(serialize=False, primary_key=True, db_column='nodeId')),
                ('name', models.CharField(max_length=255)),
                ('namespace', models.ForeignKey(to='rdfserializer.Namespace', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'nodes',
            },
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
                'db_table': 'schemes',
            },
        ),
        migrations.AddField(
            model_name='fieldrelation',
            name='node',
            field=models.ForeignKey(to='rdfserializer.Node', db_column='nodeId', on_delete=models.CASCADE),
        ),
    ]
