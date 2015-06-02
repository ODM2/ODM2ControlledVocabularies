# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    namespace = apps.get_model('rdfserializer', 'Namespace')
    node = apps.get_model('rdfserializer', 'Node')
    field_relation = apps.get_model('rdfserializer', 'FieldRelation')
    scheme = apps.get_model('rdfserializer', 'Scheme')

    db_alias = schema_editor.connection.alias

    namespace.objects.using(db_alias).bulk_create([
        namespace(alias='skos', reference='http://www.w3.org/2004/02/skos/core'),
        namespace(alias='odm2', reference='http://vocabulary.odm2.org/ODM2/ODM2Terms'),
        namespace(alias='dc', reference='http://purl.org/dc/elements/1.1/'),
    ])

    node.objects.using(db_alias).bulk_create([
        node(name='prefLabel', namespace_id='skos'),
        node(name='definition', namespace_id='skos'),
        node(name='note', namespace_id='skos'),
        node(name='historyNote', namespace_id='skos'),
        node(name='exactMatch', namespace_id='skos'),
        node(name='category', namespace_id='odm2'),
        node(name='producesResult', namespace_id='odm2'),
        node(name='Concept', namespace_id='skos'),
        node(name='inScheme', namespace_id='skos'),
        node(name='offset1', namespace_id='odm2'),
        node(name='offset2', namespace_id='odm2'),
        node(name='offset3', namespace_id='odm2'),
    ])

    field_relation.objects.using(db_alias).bulk_create([
        field_relation(field_name='name',
                       node=node.objects.using(db_alias).get(name='prefLabel', namespace_id='skos')),
        field_relation(field_name='definition',
                       node=node.objects.using(db_alias).get(name='definition', namespace_id='skos')),
        field_relation(field_name='note',
                       node=node.objects.using(db_alias).get(name='note', namespace_id='skos')),
        field_relation(field_name='provenance',
                       node=node.objects.using(db_alias).get(name='historyNote', namespace_id='skos')),
        field_relation(field_name='provenance_uri',
                       node=node.objects.using(db_alias).get(name='exactMatch', namespace_id='skos')),
        field_relation(field_name='category',
                       node=node.objects.using(db_alias).get(name='category', namespace_id='odm2')),
        field_relation(field_name='produces_result',
                       node=node.objects.using(db_alias).get(name='producesResult', namespace_id='odm2')),
        field_relation(field_name='term',
                       node=node.objects.using(db_alias).get(name='Concept', namespace_id='skos')),
        field_relation(field_name='offset1',
                       node=node.objects.using(db_alias).get(name='offset1', namespace_id='odm2')),
        field_relation(field_name='offset2',
                       node=node.objects.using(db_alias).get(name='offset2', namespace_id='odm2')),
        field_relation(field_name='offset3',
                       node=node.objects.using(db_alias).get(name='offset3', namespace_id='odm2')),
    ])

    scheme.objects.using(db_alias).bulk_create([
        scheme(name='actionType', title='ODM2 ActionType Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the type of actions performed in making observations. '
                           'Depending on the action type, the action may or may not produce an observation result.',
               uri='http://vocabulary.odm2.org/actiontype'
               ),
        scheme(name='aggregationStatistic', title='ODM2 Aggregation Statistic Controlled Vocabulary',
               creator='ODM2 Working Group',
               description='A vocabulary for describing the calculated statistic associated with recorded observations.'
                           ' The aggregation statistic is calculated over the time aggregation interval associated '
                           'with the recorded observation. ',
               uri='http://vocabulary.odm2.org/aggregationstatistic'
               ),
        scheme(name='annotationType', title='ODM2 Annotation Type Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the type of annotation. '
                           'In ODM2 the annotation type determines whether the annotation forms a grouping of '
                           'related entities (e.g., a group of sites or variables) or an annotation of a particular '
                           'entity (e.g., a comment about an individual Site or data value). ',
               uri='http://vocabulary.odm2.org/annotationtype'
               ),
        scheme(name='censorCode', title='ODM2 Censor Code Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing whether a data value was determined or whether the '
                           'actual value is unknown due to right or left censoring.',
               uri='http://vocabulary.odm2.org/censorcode'
               ),
        scheme(name='dataQualityType', title='ODM2 Controlled Vocabulary Data Quality Type CV',
               creator='ODM2 Working Group',
               description='A vocabulary for describing the type of data quality information provided '
                           'for a particular Result. Examples include the accuracy or precision of the data '
                           'values within the Result.',
               uri='http://vocabulary.odm2.org/dataqualitytype'
               ),
        scheme(name='datasetType', title='ODM2 Dataset Type Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing types of Datasets in ODM2. '
                           'Datasets are logical groupings of Results.',
               uri='http://vocabulary.odm2.org/datasettype'
               ),
        scheme(name='directiveType', title='ODM2 Directive Type Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing types of directives under which observations are made. '
                           'Examples include projects, monitoring programs, campaigns, etc.',
               uri='http://vocabulary.odm2.org/directivetype'
               ),
        scheme(name='elevationDatum', title='ODM2 Elevation Datum Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing vertical datums. Vertical datums are used in ODM2 to '
                           'specify the origin for elevations associated with SamplingFeatures.',
               uri='http://vocabulary.odm2.org/elevationdatum'
               ),
        scheme(name='equipmentType', title='ODM2 Equipment Type Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing types of equipment used for making observations. '
                           'Examples include sensors, batteries, radios, dataloggers, samplers, etc.',
               uri='http://vocabulary.odm2.org/equipmenttype'
               ),
        scheme(name='methodType', title='ODM2 MethodType Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing types of Methods associated with creating observations. '
                           'MethodTypes correspond with ActionTypes in ODM2. An Action must be performed using '
                           'an appropriate MethodType - e.g., a specimen collection Action should be associated '
                           'with a specimen collection method.',
               uri='http://vocabulary.odm2.org/methodtype'
               ),
        scheme(name='organizationType', title='ODM2 OrganizationType Controlled Vocabulary',
               creator='ODM2 Working Group',
               description='A vocabulary for describing types of Organizations. '
                           'In ODM2, People may or may not be affiliated with an Organization. '
                           'People can also be affiliated with more than one Organization.',
               uri='http://vocabulary.odm2.org/organizationtype'
               ),
        scheme(name='propertyDataType', title='ODM2 Property Data Type Controlled Vocabulary',
               creator='ODM2 Working Group',
               description='A vocabulary for describing the data type for an extension property in ODM2. '
                           'Extension properties can be added to many of the entities in '
                           'ODM2 (e.g., Sites, Variables, etc.). The values of these extension properties must '
                           'be of one of the listed primitive data types.',
               uri='http://vocabulary.odm2.org/propertydatatype'
               ),
        scheme(name='qualityCode', title='ODM2 Quality Code Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the quality of the observation.',
               uri='http://vocabulary.odm2.org/qualitycode'
               ),
        scheme(name='referenceMaterialMedium', title='ODM2 Reference Material Medium Controlled Vocabulary',
               creator='ODM2 Working Group',
               description='A vocabulary for describing the physical medium of a reference material.',
               uri='http://vocabulary.odm2.org/referencematerialmedium'
               ),
        scheme(name='relationshipType', title='ODM2 Controlled Vocabulary Relationship Type CV Relationship Type CV',
               creator='ODM2 Working Group',
               description='A vocabulary for describing the type of relationship between two entities in an'
                           ' ODM2 database. Examples include related Actions, Results, datasets, etc. '
                           'The Relationship Type describes the nature of the relationship between the two entity '
                           'instances (e.g., a Specimen SamplingFeature "was collected at" a Site SamplingFeature).',
               uri='http://vocabulary.odm2.org/relationshiptype'
               ),
        scheme(name='resultType', title='ODM2 Result Type Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the type of the Result. '
                           'In ODM2 Results are separated from, but related to their data values. '
                           'Each ResultType has a set of related tables for storing the data values '
                           'for any result of that type.',
               uri='http://vocabulary.odm2.org/resulttype'
               ),
        scheme(name='sampledMedium', title='ODM2 Sampled Medium Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the physical medium within which an observation was made. '
                           'For sensors this will be the physical medium in which the sensor is placed to '
                           'make measurements. For Specimens, this will be the physical medium that was sampled.',
               uri='http://vocabulary.odm2.org/sampledmedium'
               ),
        scheme(name='samplingFeatureGeotype', title='ODM2 Sampling Feature Geo-type Controlled Vocabulary',
               creator='ODM2 Working Group',
               description='A vocabulary for describing the geospatial feature type associated with a SamplingFeature. '
                           'For example, Site SamplingFeatures are represented as points. '
                           'In ODM2, each SamplingFeature may have only one geospatial type, but a geospatial types '
                           'may range from simple points to a complex polygons or even three dimensional volumes.',
               uri='http://vocabulary.odm2.org/samplingfeaturegeotype'
               ),
        scheme(name='samplingFeatureType', title='ODM2 Sampling Feature Type Controlled Vocabulary',
               creator='ODM2 Working Group',
               description='A vocabulary for describing the type of SamplingFeature. '
                           'Many different SamplingFeature types can be represented in ODM2. '
                           'SamplingFeatures of type Site and Specimen will be the most common, but many '
                           'different types of varying levels of complexity can be used.',
               uri='http://vocabulary.odm2.org/samplingfeaturetype'
               ),
        scheme(name='siteType', title='ODM2 Site Type Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the type of a data collection Site. '
                           'To some extent, these types represent the ultimate feature of '
                           'interest that the site was established to measure. '
                           'For example, a Stream Site was established to measure properties of a Stream.',
               uri='http://vocabulary.odm2.org/sitetype'
               ),
        scheme(name='spatialOffsetType', title='ODM2 Spatial Offset Type Controlled Vocabulary',
               creator='ODM2 Working Group',
               description='A vocabulary for describing the type of Spatial Offset '
                           'that exists between two Sampling Features.',
               uri='http://vocabulary.odm2.org/spatialoffsettype'
               ),
        scheme(name='speciation', title='ODM2 Speciation Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the type of Spatial Offset '
                           'that exists between two Sampling Features.',
               uri='http://vocabulary.odm2.org/speciation'
               ),
        scheme(name='specimenMedium', title='ODM2 Specimen Medium Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the physical medium of a physical Specimen.',
               uri='http://vocabulary.odm2.org/specimenmedium'
               ),
        scheme(name='specimenType', title='ODM2 Specimen Type Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the type of a physical Specimen.',
               uri='http://vocabulary.odm2.org/specimentype'
               ),
        scheme(name='status', title='ODM2 Status Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the data collection status of a Result. '
                           'In ODM2 the StatusCV can be used to specify whether data collection is planned, '
                           'ongoing, or complete.',
               uri='http://vocabulary.odm2.org/status'
               ),
        scheme(name='taxonomicClassifierType', title='ODM2 Taxonomic Classifier Type Controlled Vocabulary',
               creator='ODM2 Working Group',
               description='A vocabulary for describing types of taxonomies from which descriptive terms used '
                           'in an ODM2 database have been drawn. Taxonomic classifiers provide a way to classify '
                           'Results and Specimens according to terms from a formal taxonomy.',
               uri='http://vocabulary.odm2.org/taxonomicclassifiertype'
               ),
        scheme(name='variableName', title='ODM2 Variable Name Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the name of Variables.',
               uri='http://vocabulary.odm2.org/variablename'
               ),
        scheme(name='variableType', title='ODM2 Variable Type Controlled Vocabulary', creator='ODM2 Working Group',
               description='A vocabulary for describing the type of Variables. '
                           'VariableTypes provide a way to group Variables into categories for '
                           'easier querying and filtering.',
               uri='http://vocabulary.odm2.org/variabletype'
               ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('rdfserializer', 'schema_migration'),
    ]

    operations = [
        migrations.RunPython(
            forwards,
        ),
    ]
