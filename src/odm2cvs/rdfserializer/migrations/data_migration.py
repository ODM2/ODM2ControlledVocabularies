# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forwards(apps, schema_editor):
    Namespace = apps.get_model('rdfserializer', 'Namespace')
    Node = apps.get_model('rdfserializer', 'Node')
    FieldRelation = apps.get_model('rdfserializer', 'FieldRelation')
    Scheme = apps.get_model('rdfserializer', 'Scheme')

    db_alias = schema_editor.connection.alias

    Namespace.objects.using(db_alias).bulk_create([
        Namespace(alias='skos', reference='http://www.w3.org/2004/02/skos/core'),
        Namespace(alias='odm2', reference='http://vocabulary.odm.org/ODM2/ODM2Terms'),
    ])

    Node.objects.using(db_alias).bulk_create([
        Node(name='prefLabel', namespace_id='skos'),
        Node(name='definition', namespace_id='skos'),
        Node(name='note', namespace_id='skos'),
        Node(name='historyNote', namespace_id='skos'),
        Node(name='exactMatch', namespace_id='skos'),
        Node(name='category', namespace_id='odm2'),
        Node(name='producesResult', namespace_id='odm2'),
    ])

    FieldRelation.objects.using(db_alias).bulk_create([
        FieldRelation(field_name='term',
                      node=Node.objects.using(db_alias).get(name='prefLabel', namespace_id='skos')
                      ),
        FieldRelation(field_name='definition',
                      node=Node.objects.using(db_alias).get(name='definition', namespace_id='skos')
                      ),
        FieldRelation(field_name='note',
                      node=Node.objects.using(db_alias).get(name='note', namespace_id='skos')
                      ),
        FieldRelation(field_name='provenance',
                      node=Node.objects.using(db_alias).get(name='historyNote', namespace_id='skos')
                      ),
        FieldRelation(field_name='provenanceURI',
                      node=Node.objects.using(db_alias).get(name='exactMatch', namespace_id='skos')
                      ),
        FieldRelation(field_name='category',
                      node=Node.objects.using(db_alias).get(name='category', namespace_id='odm2')
                      ),
        FieldRelation(field_name='producesResult',
                      node=Node.objects.using(db_alias).get(name='producesResult', namespace_id='odm2')
                      ),
    ])

    Scheme.objects.using(db_alias).bulk_create([
        Scheme(name='actionTypeCV', title='ODM2 ActionType Controlled Vocabulary',
               description='A vocabulary for describing the types of activities that can be encoded as ODM Actions.',
               uri='http://vocabulary.odm.org/ODM2/actionTypeCV'
               ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('rdfserializer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            forwards,
        ),
    ]
