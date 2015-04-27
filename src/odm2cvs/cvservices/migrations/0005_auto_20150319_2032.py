# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvservices', '0004_auto_20150319_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actiontyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Action Type Request'},
        ),
        migrations.AlterModelOptions(
            name='aggregationstatistic',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Aggregation Statistic'},
        ),
        migrations.AlterModelOptions(
            name='aggregationstatisticrequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Aggregation Statistic Request'},
        ),
        migrations.AlterModelOptions(
            name='annotationtype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Annotation Type'},
        ),
        migrations.AlterModelOptions(
            name='annotationtyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Annotation Type Request'},
        ),
        migrations.AlterModelOptions(
            name='censorcode',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Censor Code'},
        ),
        migrations.AlterModelOptions(
            name='censorcoderequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Censor Code Request'},
        ),
        migrations.AlterModelOptions(
            name='datasettype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Dataset Type'},
        ),
        migrations.AlterModelOptions(
            name='datasettyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Dataset Type Request'},
        ),
        migrations.AlterModelOptions(
            name='directivetype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Directive Type'},
        ),
        migrations.AlterModelOptions(
            name='directivetyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Directive Type Request'},
        ),
        migrations.AlterModelOptions(
            name='elevationdatum',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Elevation Datum'},
        ),
        migrations.AlterModelOptions(
            name='elevationdatumrequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Elevation Datum Request'},
        ),
        migrations.AlterModelOptions(
            name='equipmenttype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Equipment Type'},
        ),
        migrations.AlterModelOptions(
            name='equipmenttyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Equipment Type Request'},
        ),
        migrations.AlterModelOptions(
            name='methodtype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Method Type'},
        ),
        migrations.AlterModelOptions(
            name='methodtyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Method Type Request'},
        ),
        migrations.AlterModelOptions(
            name='organizationtype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Organization Type'},
        ),
        migrations.AlterModelOptions(
            name='organizationtyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Organization Type Request'},
        ),
        migrations.AlterModelOptions(
            name='propertydatatype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Property Data Type'},
        ),
        migrations.AlterModelOptions(
            name='propertydatatyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Property Data Type Request'},
        ),
        migrations.AlterModelOptions(
            name='qualitycode',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Quality Code'},
        ),
        migrations.AlterModelOptions(
            name='qualitycoderequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Quality Code Request'},
        ),
        migrations.AlterModelOptions(
            name='referencematerialmedium',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Reference Material Medium'},
        ),
        migrations.AlterModelOptions(
            name='referencematerialmediumrequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Reference Material Medium Request'},
        ),
        migrations.AlterModelOptions(
            name='resulttype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Result Type'},
        ),
        migrations.AlterModelOptions(
            name='resulttyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Result Type Request'},
        ),
        migrations.AlterModelOptions(
            name='sampledmedium',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Sampled Medium'},
        ),
        migrations.AlterModelOptions(
            name='sampledmediumrequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Sampled Medium Request'},
        ),
        migrations.AlterModelOptions(
            name='samplingfeaturegeotype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Sampling Feature Geo-type'},
        ),
        migrations.AlterModelOptions(
            name='samplingfeaturegeotyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Sampling Feature Geo-type Request'},
        ),
        migrations.AlterModelOptions(
            name='samplingfeaturetype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Sampling Feature Type'},
        ),
        migrations.AlterModelOptions(
            name='samplingfeaturetyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Sampling Feature Type Request'},
        ),
        migrations.AlterModelOptions(
            name='sitetype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Site Type'},
        ),
        migrations.AlterModelOptions(
            name='sitetyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Site Type Request'},
        ),
        migrations.AlterModelOptions(
            name='spatialoffsettype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Spatial Offset Type'},
        ),
        migrations.AlterModelOptions(
            name='spatialoffsettyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Spatial Offset Type Request'},
        ),
        migrations.AlterModelOptions(
            name='speciation',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Speciation'},
        ),
        migrations.AlterModelOptions(
            name='speciationrequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Speciation Request'},
        ),
        migrations.AlterModelOptions(
            name='specimenmedium',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Specimen Medium'},
        ),
        migrations.AlterModelOptions(
            name='specimenmediumrequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Specimen Medium Request'},
        ),
        migrations.AlterModelOptions(
            name='specimentype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Specimen Type'},
        ),
        migrations.AlterModelOptions(
            name='specimentyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Specimen Type Request'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Status'},
        ),
        migrations.AlterModelOptions(
            name='statusrequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Status Request'},
        ),
        migrations.AlterModelOptions(
            name='taxonomicclassifiertype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Taxonomic Classifier Type'},
        ),
        migrations.AlterModelOptions(
            name='taxonomicclassifiertyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Taxonomic Classifier Type Request'},
        ),
        migrations.AlterModelOptions(
            name='variablename',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Variable Name'},
        ),
        migrations.AlterModelOptions(
            name='variablenamerequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Variable Name Request'},
        ),
        migrations.AlterModelOptions(
            name='variabletype',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Variable Type'},
        ),
        migrations.AlterModelOptions(
            name='variabletyperequest',
            options={'ordering': ['name'], 'managed': False, 'verbose_name': 'Variable Type Request'},
        ),
    ]
