from __future__ import unicode_literals
import datetime
from django.utils import timezone
from uuid import uuid4

from django.db import models


class ControlVocabulary(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.TextField()
    category = models.CharField(max_length=255, blank=True)
    provenance = models.TextField(blank=True)
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        abstract = True
        ordering = ["-name"]


class ControlVocabularyRequest(models.Model):
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    ACCEPTED = 'Accepted'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (ACCEPTED, 'Accepted'),
    )

    term = models.CharField(max_length=255, help_text="Please enter a URI-friendly version of your term with no spaces, special characters, etc.")
    name = models.CharField(max_length=255, help_text="Please enter the term as you would expect it to appear in a sentence.")
    definition = models.TextField(help_text="Please enter a detailed definition of the term.")
    category = models.CharField(max_length=255, blank=True, help_text="You may suggest a category for the term. Refer to the vocabulary to see which categories have been used. You may also suggest a new category.")
    provenance = models.TextField(blank=True, help_text="Enter a note about where the term came from. If you retrieved the definition of the term from a website or other source, note that here.")
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True, help_text="If you retrieved the term from another formal vocabulary system, enter the URI of the term from the other system here.")
    note = models.TextField(blank=True, help_text="Please enter any additional notes you may have about the term.")
    request_id = models.CharField(max_length=255, db_column='requestId', primary_key=True, default=uuid4)
    status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    date_submitted = models.DateField(db_column='dateSubmitted', default=timezone.now)
    date_status_changed = models.DateField(db_column='dateStatusChanged', default=timezone.now)
    request_notes = models.TextField(db_column='requestNotes', blank=True)
    submitter_name = models.CharField(max_length=255, db_column='submitterName', help_text="Enter your name.")
    submitter_email = models.CharField(max_length=255, db_column='submitterEmail', help_text="Enter your email address.")
    request_reason = models.CharField(max_length=255, db_column='requestReason', help_text="Please enter a brief description of the reason for your submission (e.g., Term does not exist yet, Term is needed for my data use case, etc.)")
    original_request = models.ForeignKey('self', db_column='originalRequestId', null=True)

    class Meta:
        abstract = True


class AbstractActionType(models.Model):
    PRODUCES_RESULT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    produces_result = models.CharField(db_column='producesResult', max_length=5, choices=PRODUCES_RESULT_CHOICES, blank=True)

    class Meta:
        abstract = True


class AbstractSpatialOffsetType(models.Model):
    offset1 = models.TextField(db_column='offset1', blank=True)
    offset2 = models.TextField(db_column='offset2', blank=True)
    offset3 = models.TextField(db_column='offset3', blank=True)

    class Meta:
        abstract = True

class AbstractUnitsType(models.Model):
    default_unit = models.CharField(db_column='defaultUnit', max_length=100, blank=True)
    dimension_symbol = models.CharField(db_column='dimensionSymbol', max_length=50, blank=True)
    dimension_length = models.IntegerField(db_column='dimensionLength', blank=True)
    dimension_mass = models.IntegerField(db_column='dimensionMass', blank=True)
    dimension_time = models.IntegerField(db_column='dimensionTime', blank=True)
    dimension_current = models.IntegerField(db_column='dimensionCurrent', blank=True)
    dimension_temperature = models.IntegerField(db_column='dimensionTemperature', blank=True)
    dimension_amount = models.IntegerField(db_column='dimensionAmount', blank=True)
    dimension_light = models.IntegerField(db_column='dimensionLight', blank=True)
    
    class Meta:
        abstract = True

class UnitsType(ControlVocabulary, AbstractUnitsType):
    class Meta:
        managed = False
        db_table = 'unitstypecv'
        verbose_name = 'Units Type'
        ordering = ["name"]

class UnitsTypeRequest(ControlVocabularyRequest, AbstractUnitsType):
    class Meta:
        managed = False
        db_table = 'unitstypecvrequests'
        verbose_name = 'Units Type Request'
        ordering = ["name"]

class ActionType(ControlVocabulary, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'actiontypecv'
        verbose_name = 'Action Type'
        ordering = ["name"]

class ActionTypeRequest(ControlVocabularyRequest, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'actiontypecvrequests'
        verbose_name = 'Action Type Request'
        ordering = ["name"]


class MethodType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'methodtypecv'
        verbose_name = 'Method Type'
        ordering = ["name"]


class MethodTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'methodtypecvrequests'
        verbose_name = 'Method Type Request'
        ordering = ["name"]


class OrganizationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'organizationtypecv'
        verbose_name = 'Organization Type'
        ordering = ["name"]


class OrganizationTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'organizationtypecvrequests'
        verbose_name = 'Organization Type Request'
        ordering = ["name"]


class SamplingFeatureGeotype(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'samplingfeaturegeotypecv'
        verbose_name = 'Sampling Feature Geo-type'
        ordering = ["name"]


class SamplingFeatureGeotypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'samplingfeaturegeotypecvrequests'
        verbose_name = 'Sampling Feature Geo-type Request'


class SamplingFeatureType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'samplingfeaturetypecv'
        verbose_name = 'Sampling Feature Type'


class SamplingFeatureTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'samplingfeaturetypecvrequests'
        verbose_name = 'Sampling Feature Type Request'


class SiteType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sitetypecv'
        verbose_name = 'Site Type'


class SiteTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'sitetypecvrequests'
        verbose_name = 'Site Type Request'


class AggregationStatistic(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'aggregationstatisticcv'
        verbose_name = 'Aggregation Statistic'


class AggregationStatisticRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'aggregationstatisticcvrequests'
        verbose_name = 'Aggregation Statistic Request'


class AnnotationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'annotationtypecv'
        verbose_name = 'Annotation Type'

class AnnotationTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'annotationtypecvrequests'
        verbose_name = 'Annotation Type Request'


class CensorCode(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'censorcodecv'
        verbose_name = 'Censor Code'


class CensorCodeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'censorcodecvrequests'
        verbose_name = 'Censor Code Request'


class DatasetType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'datasettypecv'
        verbose_name = 'Dataset Type'


class DatasetTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'datasettypecvrequests'
        verbose_name = 'Dataset Type Request'

class DirectiveType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'directivetypecv'
        verbose_name = 'Directive Type'


class DirectiveTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'directivetypecvrequests'
        verbose_name = 'Directive Type Request'


class ElevationDatum(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'elevationdatumcv'
        verbose_name = 'Elevation Datum'


class ElevationDatumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'elevationdatumcvrequests'
        verbose_name = 'Elevation Datum Request'


class EquipmentType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'equipmenttypecv'
        verbose_name = 'Equipment Type'


class EquipmentTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'equipmenttypecvrequests'
        verbose_name = 'Equipment Type Request'


class PropertyDataType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'propertydatatypecv'
        verbose_name = 'Property Data Type'


class PropertyDataTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'propertydatatypecvrequests'
        verbose_name = 'Property Data Type Request'


class QualityCode(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'qualitycodecv'
        verbose_name = 'Quality Code'


class QualityCodeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'qualitycodecvrequests'
        verbose_name = 'Quality Code Request'

'''
class ReferenceMaterialMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'referencematerialmediumcv'
        verbose_name = 'Reference Material Medium'
'''

class ReferenceMaterialMediumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'referencematerialmediumcvrequests'
        verbose_name = 'Reference Material Medium Request'


class ResultType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'resulttypecv'
        verbose_name = 'Result Type'


class ResultTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'resulttypecvrequests'
        verbose_name = 'Result Type Request'

'''
class SampledMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'sampledmediumcv'
        verbose_name = 'Sampled Medium'
'''

class SampledMediumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'sampledmediumcvrequests'
        verbose_name = 'Sampled Medium Request'


class SpatialOffsetType(ControlVocabulary, AbstractSpatialOffsetType):
    class Meta:
        managed = False
        db_table = 'spatialoffsettypecv'
        verbose_name = 'Spatial Offset Type'


class SpatialOffsetTypeRequest(ControlVocabularyRequest, AbstractSpatialOffsetType):
    class Meta:
        managed = False
        db_table = 'spatialoffsettypecvrequests'
        verbose_name = 'Spatial Offset Type Request'


class Speciation(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'speciationcv'
        verbose_name = 'Speciation'


class SpeciationRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'speciationcvrequests'
        verbose_name = 'Speciation Request'

'''
class SpecimenMedium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'specimenmediumcv'
        verbose_name = 'Specimen Medium'
'''

class SpecimenMediumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'specimenmediumcvrequests'
        verbose_name = 'Specimen Medium Request'


class SpecimenType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'specimentypecv'
        verbose_name = 'Specimen Type'


class SpecimenTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'specimentypecvrequests'
        verbose_name = 'Specimen Type Request'


class Status(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'statuscv'
        verbose_name = 'Status'


class StatusRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'statuscvrequests'
        verbose_name = 'Status Request'


class TaxonomicClassifierType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'taxonomicclassifiertypecv'
        verbose_name = 'Taxonomic Classifier Type'


class TaxonomicClassifierTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'taxonomicclassifiertypecvrequests'
        verbose_name = 'Taxonomic Classifier Type Request'


class VariableName(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'variablenamecv'
        verbose_name = 'Variable Name'


class VariableNameRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'variablenamecvrequests'
        verbose_name = 'Variable Name Request'


class VariableType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'variabletypecv'
        verbose_name = 'Variable Type'


class VariableTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'variabletypecvrequests'
        verbose_name = 'Variable Type Request'

class DataQualityType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'dataqualitytypecv'
        verbose_name = 'Data Quality Type'


class DataQualityTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'dataqualitytypecvrequests'
        verbose_name = 'Data Quality Type Request'


class RelationshipType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'relationshiptypecv'
        verbose_name = 'Relationship Type'


class RelationshipTypeRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'relationshiptypecvrequests'
        verbose_name = 'Relationship Type Request'

class Medium(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'mediumcv'
        verbose_name = 'Medium'

class MediumRequest(ControlVocabularyRequest):
    class Meta:
        managed = False
        db_table = 'mediumcvrequests'
        verbose_name = 'Medium Request'

