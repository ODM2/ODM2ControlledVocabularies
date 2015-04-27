# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cvservices', '0005_auto_20150319_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataQualityType',
            fields=[
                ('term', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('definition', models.TextField()),
                ('category', models.CharField(max_length=255, blank=True)),
                ('provenance', models.TextField(blank=True)),
                ('provenance_uri', models.URLField(db_column='provenanceUri', blank=True)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Data Quality Type',
                'db_table': 'dataqualitytypecv',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataQualityTypeRequest',
            fields=[
                ('term', models.CharField(help_text='Please enter a URI-friendly version of your term with no spaces, special characters, etc.', max_length=255)),
                ('name', models.CharField(help_text='Please enter the term as you would expect it to appear in a sentence.', max_length=255)),
                ('definition', models.TextField(help_text='Please enter a detailed definition of the term.')),
                ('category', models.CharField(help_text='You may suggest a category for the term. Refer to the vocabulary to see which categories have been used. You may also suggest a new category.', max_length=255, blank=True)),
                ('provenance', models.TextField(help_text='Enter a note about where the term came from. If you retrieved the definition of the term from a website or other source, note that here.', blank=True)),
                ('provenance_uri', models.URLField(help_text='If you retrieved the term from another formal vocabulary system, enter the URI of the term from the other system here.', db_column='provenanceUri', blank=True)),
                ('note', models.TextField(help_text='Please enter any additional notes you may have about the term.', blank=True)),
                ('request_id', models.CharField(default=uuid.uuid4, max_length=255, serialize=False, primary_key=True, db_column='requestId')),
                ('status', models.CharField(default='Pending', max_length=255, db_column='status', choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')])),
                ('date_submitted', models.DateField(default=django.utils.timezone.now, db_column='dateSubmitted')),
                ('date_status_changed', models.DateField(default=django.utils.timezone.now, db_column='dateStatusChanged')),
                ('request_notes', models.TextField(db_column='requestNotes', blank=True)),
                ('submitter_name', models.CharField(help_text='Enter your name.', max_length=255, db_column='submitterName')),
                ('submitter_email', models.CharField(help_text='Enter your email address.', max_length=255, db_column='submitterEmail')),
                ('request_reason', models.CharField(help_text='Please enter a brief description of the reason for your submission (e.g., Term does not exist yet, Term is needed for my data use case, etc.)', max_length=255, db_column='requestReason')),
            ],
            options={
                'verbose_name': 'Data Quality Type Request',
                'db_table': 'dataqualitytypecvrequests',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('term', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('definition', models.TextField()),
                ('category', models.CharField(max_length=255, blank=True)),
                ('provenance', models.TextField(blank=True)),
                ('provenance_uri', models.URLField(db_column='provenanceUri', blank=True)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Relationship Type',
                'db_table': 'relationshiptypecv',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelationshipTypeRequest',
            fields=[
                ('term', models.CharField(help_text='Please enter a URI-friendly version of your term with no spaces, special characters, etc.', max_length=255)),
                ('name', models.CharField(help_text='Please enter the term as you would expect it to appear in a sentence.', max_length=255)),
                ('definition', models.TextField(help_text='Please enter a detailed definition of the term.')),
                ('category', models.CharField(help_text='You may suggest a category for the term. Refer to the vocabulary to see which categories have been used. You may also suggest a new category.', max_length=255, blank=True)),
                ('provenance', models.TextField(help_text='Enter a note about where the term came from. If you retrieved the definition of the term from a website or other source, note that here.', blank=True)),
                ('provenance_uri', models.URLField(help_text='If you retrieved the term from another formal vocabulary system, enter the URI of the term from the other system here.', db_column='provenanceUri', blank=True)),
                ('note', models.TextField(help_text='Please enter any additional notes you may have about the term.', blank=True)),
                ('request_id', models.CharField(default=uuid.uuid4, max_length=255, serialize=False, primary_key=True, db_column='requestId')),
                ('status', models.CharField(default='Pending', max_length=255, db_column='status', choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')])),
                ('date_submitted', models.DateField(default=django.utils.timezone.now, db_column='dateSubmitted')),
                ('date_status_changed', models.DateField(default=django.utils.timezone.now, db_column='dateStatusChanged')),
                ('request_notes', models.TextField(db_column='requestNotes', blank=True)),
                ('submitter_name', models.CharField(help_text='Enter your name.', max_length=255, db_column='submitterName')),
                ('submitter_email', models.CharField(help_text='Enter your email address.', max_length=255, db_column='submitterEmail')),
                ('request_reason', models.CharField(help_text='Please enter a brief description of the reason for your submission (e.g., Term does not exist yet, Term is needed for my data use case, etc.)', max_length=255, db_column='requestReason')),
            ],
            options={
                'verbose_name': 'Relationship Type Request',
                'db_table': 'relationshiptypecvrequests',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='aggregationstatistic',
            options={'managed': False, 'verbose_name': 'Aggregation Statistic'},
        ),
        migrations.AlterModelOptions(
            name='aggregationstatisticrequest',
            options={'managed': False, 'verbose_name': 'Aggregation Statistic Request'},
        ),
        migrations.AlterModelOptions(
            name='annotationtype',
            options={'managed': False, 'verbose_name': 'Annotation Type'},
        ),
        migrations.AlterModelOptions(
            name='annotationtyperequest',
            options={'managed': False, 'verbose_name': 'Annotation Type Request'},
        ),
        migrations.AlterModelOptions(
            name='censorcode',
            options={'managed': False, 'verbose_name': 'Censor Code'},
        ),
        migrations.AlterModelOptions(
            name='censorcoderequest',
            options={'managed': False, 'verbose_name': 'Censor Code Request'},
        ),
        migrations.AlterModelOptions(
            name='datasettype',
            options={'managed': False, 'verbose_name': 'Dataset Type'},
        ),
        migrations.AlterModelOptions(
            name='datasettyperequest',
            options={'managed': False, 'verbose_name': 'Dataset Type Request'},
        ),
        migrations.AlterModelOptions(
            name='directivetype',
            options={'managed': False, 'verbose_name': 'Directive Type'},
        ),
        migrations.AlterModelOptions(
            name='directivetyperequest',
            options={'managed': False, 'verbose_name': 'Directive Type Request'},
        ),
        migrations.AlterModelOptions(
            name='elevationdatum',
            options={'managed': False, 'verbose_name': 'Elevation Datum'},
        ),
        migrations.AlterModelOptions(
            name='elevationdatumrequest',
            options={'managed': False, 'verbose_name': 'Elevation Datum Request'},
        ),
        migrations.AlterModelOptions(
            name='equipmenttype',
            options={'managed': False, 'verbose_name': 'Equipment Type'},
        ),
        migrations.AlterModelOptions(
            name='equipmenttyperequest',
            options={'managed': False, 'verbose_name': 'Equipment Type Request'},
        ),
        migrations.AlterModelOptions(
            name='propertydatatype',
            options={'managed': False, 'verbose_name': 'Property Data Type'},
        ),
        migrations.AlterModelOptions(
            name='propertydatatyperequest',
            options={'managed': False, 'verbose_name': 'Property Data Type Request'},
        ),
        migrations.AlterModelOptions(
            name='qualitycode',
            options={'managed': False, 'verbose_name': 'Quality Code'},
        ),
        migrations.AlterModelOptions(
            name='qualitycoderequest',
            options={'managed': False, 'verbose_name': 'Quality Code Request'},
        ),
        migrations.AlterModelOptions(
            name='referencematerialmedium',
            options={'managed': False, 'verbose_name': 'Reference Material Medium'},
        ),
        migrations.AlterModelOptions(
            name='referencematerialmediumrequest',
            options={'managed': False, 'verbose_name': 'Reference Material Medium Request'},
        ),
        migrations.AlterModelOptions(
            name='resulttype',
            options={'managed': False, 'verbose_name': 'Result Type'},
        ),
        migrations.AlterModelOptions(
            name='resulttyperequest',
            options={'managed': False, 'verbose_name': 'Result Type Request'},
        ),
        migrations.AlterModelOptions(
            name='sampledmedium',
            options={'managed': False, 'verbose_name': 'Sampled Medium'},
        ),
        migrations.AlterModelOptions(
            name='sampledmediumrequest',
            options={'managed': False, 'verbose_name': 'Sampled Medium Request'},
        ),
        migrations.AlterModelOptions(
            name='samplingfeaturegeotyperequest',
            options={'managed': False, 'verbose_name': 'Sampling Feature Geo-type Request'},
        ),
        migrations.AlterModelOptions(
            name='samplingfeaturetype',
            options={'managed': False, 'verbose_name': 'Sampling Feature Type'},
        ),
        migrations.AlterModelOptions(
            name='samplingfeaturetyperequest',
            options={'managed': False, 'verbose_name': 'Sampling Feature Type Request'},
        ),
        migrations.AlterModelOptions(
            name='sitetype',
            options={'managed': False, 'verbose_name': 'Site Type'},
        ),
        migrations.AlterModelOptions(
            name='sitetyperequest',
            options={'managed': False, 'verbose_name': 'Site Type Request'},
        ),
        migrations.AlterModelOptions(
            name='spatialoffsettype',
            options={'managed': False, 'verbose_name': 'Spatial Offset Type'},
        ),
        migrations.AlterModelOptions(
            name='spatialoffsettyperequest',
            options={'managed': False, 'verbose_name': 'Spatial Offset Type Request'},
        ),
        migrations.AlterModelOptions(
            name='speciation',
            options={'managed': False, 'verbose_name': 'Speciation'},
        ),
        migrations.AlterModelOptions(
            name='speciationrequest',
            options={'managed': False, 'verbose_name': 'Speciation Request'},
        ),
        migrations.AlterModelOptions(
            name='specimenmedium',
            options={'managed': False, 'verbose_name': 'Specimen Medium'},
        ),
        migrations.AlterModelOptions(
            name='specimenmediumrequest',
            options={'managed': False, 'verbose_name': 'Specimen Medium Request'},
        ),
        migrations.AlterModelOptions(
            name='specimentype',
            options={'managed': False, 'verbose_name': 'Specimen Type'},
        ),
        migrations.AlterModelOptions(
            name='specimentyperequest',
            options={'managed': False, 'verbose_name': 'Specimen Type Request'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'managed': False, 'verbose_name': 'Status'},
        ),
        migrations.AlterModelOptions(
            name='statusrequest',
            options={'managed': False, 'verbose_name': 'Status Request'},
        ),
        migrations.AlterModelOptions(
            name='taxonomicclassifiertype',
            options={'managed': False, 'verbose_name': 'Taxonomic Classifier Type'},
        ),
        migrations.AlterModelOptions(
            name='taxonomicclassifiertyperequest',
            options={'managed': False, 'verbose_name': 'Taxonomic Classifier Type Request'},
        ),
        migrations.AlterModelOptions(
            name='variablename',
            options={'managed': False, 'verbose_name': 'Variable Name'},
        ),
        migrations.AlterModelOptions(
            name='variablenamerequest',
            options={'managed': False, 'verbose_name': 'Variable Name Request'},
        ),
        migrations.AlterModelOptions(
            name='variabletype',
            options={'managed': False, 'verbose_name': 'Variable Type'},
        ),
        migrations.AlterModelOptions(
            name='variabletyperequest',
            options={'managed': False, 'verbose_name': 'Variable Type Request'},
        ),
    ]
