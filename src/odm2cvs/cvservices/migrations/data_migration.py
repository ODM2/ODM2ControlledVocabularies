# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import os

from django.db import migrations
from django.db.models.fields import IntegerField

from cvinterface import control_vocabularies


def get_data(path):
    data = []
    filename = path + '.csv'
    with open(filename, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, dialect=csv.excel)
        for line in csv_reader:
            data.append([unicode(field, 'utf-8') for field in line])

        field_names = data.pop(0)
        return map(lambda row: dict(zip(field_names, row)), data)


def map_data(Model, data, db_alias='default'):
    for term_data in data:
        term = Model()

        for field in Model._meta.fields:
            field_name = field.db_column or field.attname
            if field_name in term_data:
                value = term_data[field_name] or (0 if isinstance(field, IntegerField) else u'')
                setattr(term, field.attname, value)

        term.save(using=db_alias)


def forwards(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    data_path = os.path.abspath(os.path.dirname(__file__))

    unit_data = get_data(os.path.join(data_path, 'data', 'units'))
    map_data(apps.get_model('cvservices', 'Unit'), unit_data, db_alias)

    for vocabulary_name, vocabulary in control_vocabularies.vocabularies.iteritems():
        data = get_data(os.path.join(data_path, 'data', vocabulary_name))
        map_data(vocabulary['model'], data, db_alias)

class Migration(migrations.Migration):
    dependencies = [
        ('cvservices', 'schema_migration'),
    ]

    operations = [
        migrations.RunPython(
            forwards,
        ),
    ]
