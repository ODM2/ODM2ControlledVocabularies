# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlledVocabulary',
            fields=[
                ('vocabulary_id', models.AutoField(serialize=False, primary_key=True)),
                ('term', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('definition', models.TextField()),
                ('category', models.CharField(max_length=255, blank=True)),
                ('provenance', models.TextField(blank=True)),
                ('provenance_uri', models.URLField(db_column='provenanceUri', blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('vocabulary_status', models.CharField(default='Current', max_length=255, db_column='status', choices=[('Current', 'Current'), ('Archived', 'Archived')])),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'controlledvocabularies',
            },
        ),
        migrations.CreateModel(
            name='ControlledVocabularyRequest',
            fields=[
                ('request_id', models.AutoField(max_length=255, serialize=False, primary_key=True, db_column='requestId')),
                ('term', models.CharField(help_text='Please enter a URI-friendly version of your term with no spaces, special characters, etc.', max_length=255)),
                ('name', models.CharField(help_text='Please enter the term as you would expect it to appear in a sentence.', max_length=255)),
                ('definition', models.TextField(help_text='Please enter a detailed definition of the term.', blank=True)),
                ('category', models.CharField(help_text='You may suggest a category for the term. Refer to the vocabulary to see which categories have been used. You may also suggest a new category.', max_length=255, blank=True)),
                ('provenance', models.TextField(help_text='Enter a note about where the term came from. If you retrieved the definition of the term from a website or other source, note that here.', blank=True)),
                ('provenance_uri', models.URLField(help_text='If you retrieved the term from another formal vocabulary system, enter the URI of the term from the other system here.', max_length=1024, db_column='provenanceUri', blank=True)),
                ('note', models.TextField(help_text='Please enter any additional notes you may have about the term.', null=True, blank=True)),
                ('status', models.CharField(default='Pending', max_length=255, db_column='status', choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Archived', 'Archived')])),
                ('date_submitted', models.DateField(default=django.utils.timezone.now, db_column='dateSubmitted')),
                ('date_status_changed', models.DateField(default=django.utils.timezone.now, db_column='dateStatusChanged')),
                ('request_notes', models.TextField(db_column='requestNotes', blank=True)),
                ('submitter_name', models.CharField(help_text='Enter your name.', max_length=255, db_column='submitterName')),
                ('submitter_email', models.CharField(help_text='Enter your email address.', max_length=255, db_column='submitterEmail')),
                ('request_reason', models.TextField(help_text='Please enter a brief description of the reason for your submission (e.g., Term does not exist yet, Term is needed for my data use case, etc.)', db_column='requestReason')),
            ],
            options={
                'ordering': ['date_submitted', '-request_id'],
                'db_table': 'requests',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_id', models.AutoField(serialize=False, primary_key=True)),
                ('term', models.CharField(max_length=255, db_column='Term')),
                ('type', models.CharField(max_length=255, db_column='UnitsTypeCV')),
                ('abbreviation', models.CharField(max_length=255, db_column='UnitsAbbreviation', blank=True)),
                ('name', models.CharField(max_length=255, db_column='UnitsName')),
                ('link', models.URLField(max_length=1024, db_column='UnitsLink', blank=True)),
            ],
            options={
                'ordering': ['type'],
                'db_table': 'units',
            },
        ),
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
                ('produces_result', models.CharField(blank=True, max_length=5, db_column='producesResult', choices=[('Yes', 'Yes'), ('No', 'No')])),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'actiontypecv',
                'verbose_name': 'Action Type',
            },
            bases=('cvservices.controlledvocabulary', models.Model),
        ),
        migrations.CreateModel(
            name='ActionTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
                ('produces_result', models.CharField(blank=True, max_length=5, db_column='producesResult', choices=[('Yes', 'Yes'), ('No', 'No')])),
            ],
            options={
                'db_table': 'actiontypecvrequests',
                'verbose_name': 'Action Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest', models.Model),
        ),
        migrations.CreateModel(
            name='AggregationStatistic',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'aggregationstatisticcv',
                'verbose_name': 'Aggregation Statistic',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='AggregationStatisticRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'aggregationstatisticcvrequests',
                'verbose_name': 'Aggregation Statistic Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='AnnotationType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'annotationtypecv',
                'verbose_name': 'Annotation Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='AnnotationTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'annotationtypecvrequests',
                'verbose_name': 'Annotation Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='CensorCode',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'censorcodecv',
                'verbose_name': 'Censor Code',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='CensorCodeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'censorcodecvrequests',
                'verbose_name': 'Censor Code Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='DataQualityType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'dataqualitytypecv',
                'verbose_name': 'Data Quality Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='DataQualityTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'dataqualitytypecvrequests',
                'verbose_name': 'Data Quality Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='DatasetType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'datasettypecv',
                'verbose_name': 'Dataset Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='DatasetTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'datasettypecvrequests',
                'verbose_name': 'Dataset Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='DirectiveType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'directivetypecv',
                'verbose_name': 'Directive Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='DirectiveTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'directivetypecvrequests',
                'verbose_name': 'Directive Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='ElevationDatum',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'elevationdatumcv',
                'verbose_name': 'Elevation Datum',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='ElevationDatumRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'elevationdatumcvrequests',
                'verbose_name': 'Elevation Datum Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'equipmenttypecv',
                'verbose_name': 'Equipment Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='EquipmentTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'equipmenttypecvrequests',
                'verbose_name': 'Equipment Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'mediumcv',
                'verbose_name': 'Medium',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='MediumRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'mediumcvrequests',
                'verbose_name': 'Medium Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='MethodType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'methodtypecv',
                'verbose_name': 'Method Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='MethodTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'methodtypecvrequests',
                'verbose_name': 'Method Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'organizationtypecv',
                'verbose_name': 'Organization Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='OrganizationTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'organizationtypecvrequests',
                'verbose_name': 'Organization Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='PropertyDataType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'propertydatatypecv',
                'verbose_name': 'Property Data Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='PropertyDataTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'propertydatatypecvrequests',
                'verbose_name': 'Property Data Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='QualityCode',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'qualitycodecv',
                'verbose_name': 'Quality Code',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='QualityCodeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'qualitycodecvrequests',
                'verbose_name': 'Quality Code Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='ReferenceMaterialMediumRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'referencematerialmediumcvrequests',
                'verbose_name': 'Reference Material Medium Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'relationshiptypecv',
                'verbose_name': 'Relationship Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='RelationshipTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'relationshiptypecvrequests',
                'verbose_name': 'Relationship Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='ResultType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'resulttypecv',
                'verbose_name': 'Result Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='ResultTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'resulttypecvrequests',
                'verbose_name': 'Result Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='SampledMediumRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'sampledmediumcvrequests',
                'verbose_name': 'Sampled Medium Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='SamplingFeatureGeotype',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'samplingfeaturegeotypecv',
                'verbose_name': 'Sampling Feature Geo-type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='SamplingFeatureGeotypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'samplingfeaturegeotypecvrequests',
                'verbose_name': 'Sampling Feature Geo-type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='SamplingFeatureType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'samplingfeaturetypecv',
                'verbose_name': 'Sampling Feature Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='SamplingFeatureTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'samplingfeaturetypecvrequests',
                'verbose_name': 'Sampling Feature Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='SiteType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'sitetypecv',
                'verbose_name': 'Site Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='SiteTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'sitetypecvrequests',
                'verbose_name': 'Site Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='SpatialOffsetType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
                ('offset1', models.TextField(db_column='offset1', blank=True)),
                ('offset2', models.TextField(db_column='offset2', blank=True)),
                ('offset3', models.TextField(db_column='offset3', blank=True)),
            ],
            options={
                'db_table': 'spatialoffsettypecv',
                'verbose_name': 'Spatial Offset Type',
            },
            bases=('cvservices.controlledvocabulary', models.Model),
        ),
        migrations.CreateModel(
            name='SpatialOffsetTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
                ('offset1', models.TextField(db_column='offset1', blank=True)),
                ('offset2', models.TextField(db_column='offset2', blank=True)),
                ('offset3', models.TextField(db_column='offset3', blank=True)),
            ],
            options={
                'db_table': 'spatialoffsettypecvrequests',
                'verbose_name': 'Spatial Offset Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest', models.Model),
        ),
        migrations.CreateModel(
            name='Speciation',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'speciationcv',
                'verbose_name': 'Speciation',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='SpeciationRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'speciationcvrequests',
                'verbose_name': 'Speciation Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='SpecimenMediumRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'specimenmediumcvrequests',
                'verbose_name': 'Specimen Medium Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='SpecimenType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'specimentypecv',
                'verbose_name': 'Specimen Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='SpecimenTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'specimentypecvrequests',
                'verbose_name': 'Specimen Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'statuscv',
                'verbose_name': 'Status',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='StatusRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'statuscvrequests',
                'verbose_name': 'Status Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='TaxonomicClassifierType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'taxonomicclassifiertypecv',
                'verbose_name': 'Taxonomic Classifier Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='TaxonomicClassifierTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'taxonomicclassifiertypecvrequests',
                'verbose_name': 'Taxonomic Classifier Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='UnitsType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
                ('default_unit', models.CharField(max_length=100, db_column='defaultUnit', blank=True)),
                ('dimension_symbol', models.CharField(max_length=50, db_column='dimensionSymbol', blank=True)),
                ('dimension_length', models.IntegerField(null=True, db_column='dimensionLength', blank=True)),
                ('dimension_mass', models.IntegerField(null=True, db_column='dimensionMass', blank=True)),
                ('dimension_time', models.IntegerField(null=True, db_column='dimensionTime', blank=True)),
                ('dimension_current', models.IntegerField(null=True, db_column='dimensionCurrent', blank=True)),
                ('dimension_temperature', models.IntegerField(null=True, db_column='dimensionTemperature', blank=True)),
                ('dimension_amount', models.IntegerField(null=True, db_column='dimensionAmount', blank=True)),
                ('dimension_light', models.IntegerField(null=True, db_column='dimensionLight', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'unitstypecv',
                'verbose_name': 'Units Type',
            },
            bases=('cvservices.controlledvocabulary', models.Model),
        ),
        migrations.CreateModel(
            name='UnitsTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
                ('default_unit', models.CharField(max_length=100, db_column='defaultUnit', blank=True)),
                ('dimension_symbol', models.CharField(max_length=50, db_column='dimensionSymbol', blank=True)),
                ('dimension_length', models.IntegerField(null=True, db_column='dimensionLength', blank=True)),
                ('dimension_mass', models.IntegerField(null=True, db_column='dimensionMass', blank=True)),
                ('dimension_time', models.IntegerField(null=True, db_column='dimensionTime', blank=True)),
                ('dimension_current', models.IntegerField(null=True, db_column='dimensionCurrent', blank=True)),
                ('dimension_temperature', models.IntegerField(null=True, db_column='dimensionTemperature', blank=True)),
                ('dimension_amount', models.IntegerField(null=True, db_column='dimensionAmount', blank=True)),
                ('dimension_light', models.IntegerField(null=True, db_column='dimensionLight', blank=True)),
            ],
            options={
                'db_table': 'unitstypecvrequests',
                'verbose_name': 'Units Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest', models.Model),
        ),
        migrations.CreateModel(
            name='VariableName',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'variablenamecv',
                'verbose_name': 'Variable Name',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='VariableNameRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'variablenamecvrequests',
                'verbose_name': 'Variable Name Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.CreateModel(
            name='VariableType',
            fields=[
                ('controlledvocabulary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabulary')),
            ],
            options={
                'db_table': 'variabletypecv',
                'verbose_name': 'Variable Type',
            },
            bases=('cvservices.controlledvocabulary',),
        ),
        migrations.CreateModel(
            name='VariableTypeRequest',
            fields=[
                ('controlledvocabularyrequest_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cvservices.ControlledVocabularyRequest')),
            ],
            options={
                'db_table': 'variabletypecvrequests',
                'verbose_name': 'Variable Type Request',
            },
            bases=('cvservices.controlledvocabularyrequest',),
        ),
        migrations.AddField(
            model_name='controlledvocabularyrequest',
            name='original_request',
            field=models.ForeignKey(db_column='originalRequestId', to='cvservices.ControlledVocabularyRequest', null=True),
        ),
        migrations.AddField(
            model_name='controlledvocabularyrequest',
            name='request_for',
            field=models.ForeignKey(db_column='requestFor', blank=True, to='cvservices.ControlledVocabulary', null=True),
        ),
        migrations.AddField(
            model_name='controlledvocabulary',
            name='previous_version',
            field=models.OneToOneField(related_name='revised_version', null=True, to='cvservices.ControlledVocabulary'),
        ),
    ]
