from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from django.db import models


class ControlledVocabulary(models.Model):
    CURRENT = 'Current'
    ARCHIVED = 'Archived'

    STATUS_CHOICES = [
        (CURRENT, 'Current'),
        (ARCHIVED, 'Archived')
    ]

    vocabulary_id = models.AutoField(primary_key=True)
    term = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    definition = models.TextField()
    category = models.CharField(max_length=255, blank=True, null=True)
    provenance = models.TextField(blank=True, null=True)
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    vocabulary_status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=CURRENT)
    previous_version = models.OneToOneField('self', null=True, related_name='revised_version', on_delete=models.CASCADE)

    def has_revision(self):
        revision = None
        try:
            revision = self.revised_version
        except ObjectDoesNotExist:
            pass
        return revision is not None

    def get_latest_version(self):
        term = self
        while term.has_revision():
            term = term.revised_version
        return term

    class Meta:
        db_table = 'controlledvocabularies'
        ordering = ["name"]


class ControlledVocabularyRequest(models.Model):
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    ACCEPTED = 'Accepted'
    ARCHIVED = 'Archived'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (ACCEPTED, 'Accepted'),
        (ARCHIVED, 'Archived'),
    ]

    request_id = models.AutoField(max_length=255, db_column='requestId', primary_key=True)

    term = models.CharField(max_length=255, help_text="Please enter a URI-friendly version of your term with no spaces, special characters, etc.")
    name = models.CharField(max_length=255, help_text="Please enter the term as you would expect it to appear in a sentence.")
    definition = models.TextField(help_text="Please enter a detailed definition of the term.", blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True, help_text="You may suggest a category for the term. Refer to the vocabulary to see which categories have been used. You may also suggest a new category.")
    provenance = models.TextField(blank=True, null=True, help_text="Enter a note about where the term came from. If you retrieved the definition of the term from a website or other source, note that here.")
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True, null=True, max_length=1024, help_text="If you retrieved the term from another formal vocabulary system, enter the URI of the term from the other system here.")
    note = models.TextField(blank=True, null=True, help_text="Please enter any additional notes you may have about the term.")

    status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=PENDING)
    date_submitted = models.DateField(db_column='dateSubmitted', default=timezone.now)
    date_status_changed = models.DateField(db_column='dateStatusChanged', default=timezone.now)
    request_notes = models.TextField(db_column='requestNotes', blank=True, null=True)
    submitter_name = models.CharField(max_length=255, db_column='submitterName', help_text="Enter your name.")
    submitter_email = models.CharField(max_length=255, db_column='submitterEmail', help_text="Enter your email address.")
    request_reason = models.TextField(db_column='requestReason', help_text="Please enter a brief description of the reason for your submission (e.g., Term does not exist yet, Term is needed for my data use case, etc.)")

    request_for = models.ForeignKey('ControlledVocabulary', db_column='requestFor', blank=True, null=True, on_delete=models.CASCADE)
    original_request = models.ForeignKey('self', db_column='originalRequestId', null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'requests'
        ordering = ["date_submitted", "-request_id"]


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    term = models.CharField(max_length=255, db_column='Term')
    type = models.CharField(max_length=255, db_column='UnitsTypeCV')
    abbreviation = models.CharField(max_length=255, blank=True, null=True, db_column='UnitsAbbreviation')
    name = models.CharField(max_length=255, db_column='UnitsName')
    link = models.URLField(max_length=1024, blank=True, null=True, db_column='UnitsLink')

    class Meta:
        db_table = 'units'
        ordering = ["type"]


class AbstractActionType(models.Model):
    PRODUCES_RESULT_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
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
    dimension_length = models.IntegerField(db_column='dimensionLength', blank=True, null=True)
    dimension_mass = models.IntegerField(db_column='dimensionMass', blank=True, null=True)
    dimension_time = models.IntegerField(db_column='dimensionTime', blank=True, null=True)
    dimension_current = models.IntegerField(db_column='dimensionCurrent', blank=True, null=True)
    dimension_temperature = models.IntegerField(db_column='dimensionTemperature', blank=True, null=True)
    dimension_amount = models.IntegerField(db_column='dimensionAmount', blank=True, null=True)
    dimension_light = models.IntegerField(db_column='dimensionLight', blank=True, null=True)
    
    class Meta:
        abstract = True


class UnitsType(ControlledVocabulary, AbstractUnitsType):
    class Meta:
        db_table = 'unitstypecv'
        verbose_name = 'Units Type'
        ordering = ["name"]


class UnitsTypeRequest(ControlledVocabularyRequest, AbstractUnitsType):
    class Meta:
        db_table = 'unitstypecvrequests'
        verbose_name = 'Units Type Request'


class ActionType(ControlledVocabulary, AbstractActionType):
    class Meta:
        db_table = 'actiontypecv'
        verbose_name = 'Action Type'
        ordering = ["name"]


class ActionTypeRequest(ControlledVocabularyRequest, AbstractActionType):
    class Meta:
        db_table = 'actiontypecvrequests'
        verbose_name = 'Action Type Request'


class MethodType(ControlledVocabulary):
    class Meta:
        db_table = 'methodtypecv'
        verbose_name = 'Method Type'
        ordering = ["name"]


class MethodTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'methodtypecvrequests'
        verbose_name = 'Method Type Request'


class OrganizationType(ControlledVocabulary):
    class Meta:
        db_table = 'organizationtypecv'
        verbose_name = 'Organization Type'
        ordering = ["name"]


class OrganizationTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'organizationtypecvrequests'
        verbose_name = 'Organization Type Request'


class SamplingFeatureGeotype(ControlledVocabulary):
    class Meta:
        db_table = 'samplingfeaturegeotypecv'
        verbose_name = 'Sampling Feature Geo-type'
        ordering = ["name"]


class SamplingFeatureGeotypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'samplingfeaturegeotypecvrequests'
        verbose_name = 'Sampling Feature Geo-type Request'


class SamplingFeatureType(ControlledVocabulary):
    class Meta:
        db_table = 'samplingfeaturetypecv'
        verbose_name = 'Sampling Feature Type'


class SamplingFeatureTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'samplingfeaturetypecvrequests'
        verbose_name = 'Sampling Feature Type Request'


class SiteType(ControlledVocabulary):
    class Meta:
        db_table = 'sitetypecv'
        verbose_name = 'Site Type'


class SiteTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'sitetypecvrequests'
        verbose_name = 'Site Type Request'


class AggregationStatistic(ControlledVocabulary):
    class Meta:
        db_table = 'aggregationstatisticcv'
        verbose_name = 'Aggregation Statistic'


class AggregationStatisticRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'aggregationstatisticcvrequests'
        verbose_name = 'Aggregation Statistic Request'


class AnnotationType(ControlledVocabulary):
    class Meta:
        db_table = 'annotationtypecv'
        verbose_name = 'Annotation Type'


class AnnotationTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'annotationtypecvrequests'
        verbose_name = 'Annotation Type Request'


class CensorCode(ControlledVocabulary):
    class Meta:
        db_table = 'censorcodecv'
        verbose_name = 'Censor Code'


class CensorCodeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'censorcodecvrequests'
        verbose_name = 'Censor Code Request'


class DatasetType(ControlledVocabulary):
    class Meta:
        db_table = 'datasettypecv'
        verbose_name = 'Dataset Type'


class DatasetTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'datasettypecvrequests'
        verbose_name = 'Dataset Type Request'


class DirectiveType(ControlledVocabulary):
    class Meta:
        db_table = 'directivetypecv'
        verbose_name = 'Directive Type'


class DirectiveTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'directivetypecvrequests'
        verbose_name = 'Directive Type Request'


class ElevationDatum(ControlledVocabulary):
    class Meta:
        db_table = 'elevationdatumcv'
        verbose_name = 'Elevation Datum'


class ElevationDatumRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'elevationdatumcvrequests'
        verbose_name = 'Elevation Datum Request'


class EquipmentType(ControlledVocabulary):
    class Meta:
        db_table = 'equipmenttypecv'
        verbose_name = 'Equipment Type'


class EquipmentTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'equipmenttypecvrequests'
        verbose_name = 'Equipment Type Request'


class PropertyDataType(ControlledVocabulary):
    class Meta:
        db_table = 'propertydatatypecv'
        verbose_name = 'Property Data Type'


class PropertyDataTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'propertydatatypecvrequests'
        verbose_name = 'Property Data Type Request'


class QualityCode(ControlledVocabulary):
    class Meta:
        db_table = 'qualitycodecv'
        verbose_name = 'Quality Code'


class QualityCodeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'qualitycodecvrequests'
        verbose_name = 'Quality Code Request'

'''
class ReferenceMaterialMedium(ControlledVocabulary):
    class Meta:
        db_table = 'referencematerialmediumcv'
        verbose_name = 'Reference Material Medium'
'''


class ReferenceMaterialMediumRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'referencematerialmediumcvrequests'
        verbose_name = 'Reference Material Medium Request'


class ResultType(ControlledVocabulary):
    class Meta:
        db_table = 'resulttypecv'
        verbose_name = 'Result Type'


class ResultTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'resulttypecvrequests'
        verbose_name = 'Result Type Request'

'''
class SampledMedium(ControlledVocabulary):
    class Meta:
        db_table = 'sampledmediumcv'
        verbose_name = 'Sampled Medium'
'''


class SampledMediumRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'sampledmediumcvrequests'
        verbose_name = 'Sampled Medium Request'


class SpatialOffsetType(ControlledVocabulary, AbstractSpatialOffsetType):
    class Meta:
        db_table = 'spatialoffsettypecv'
        verbose_name = 'Spatial Offset Type'


class SpatialOffsetTypeRequest(ControlledVocabularyRequest, AbstractSpatialOffsetType):
    class Meta:
        db_table = 'spatialoffsettypecvrequests'
        verbose_name = 'Spatial Offset Type Request'


class Speciation(ControlledVocabulary):
    class Meta:
        db_table = 'speciationcv'
        verbose_name = 'Speciation'


class SpeciationRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'speciationcvrequests'
        verbose_name = 'Speciation Request'

'''
class SpecimenMedium(ControlledVocabulary):
    class Meta:
        db_table = 'specimenmediumcv'
        verbose_name = 'Specimen Medium'
'''


class SpecimenMediumRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'specimenmediumcvrequests'
        verbose_name = 'Specimen Medium Request'


class SpecimenType(ControlledVocabulary):
    class Meta:
        db_table = 'specimentypecv'
        verbose_name = 'Specimen Type'


class SpecimenTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'specimentypecvrequests'
        verbose_name = 'Specimen Type Request'


class Status(ControlledVocabulary):
    class Meta:
        db_table = 'statuscv'
        verbose_name = 'Status'


class StatusRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'statuscvrequests'
        verbose_name = 'Status Request'


class TaxonomicClassifierType(ControlledVocabulary):
    class Meta:
        db_table = 'taxonomicclassifiertypecv'
        verbose_name = 'Taxonomic Classifier Type'


class TaxonomicClassifierTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'taxonomicclassifiertypecvrequests'
        verbose_name = 'Taxonomic Classifier Type Request'


class VariableName(ControlledVocabulary):
    class Meta:
        db_table = 'variablenamecv'
        verbose_name = 'Variable Name'


class VariableNameRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'variablenamecvrequests'
        verbose_name = 'Variable Name Request'


class VariableType(ControlledVocabulary):
    class Meta:
        db_table = 'variabletypecv'
        verbose_name = 'Variable Type'


class VariableTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'variabletypecvrequests'
        verbose_name = 'Variable Type Request'


class DataQualityType(ControlledVocabulary):
    class Meta:
        db_table = 'dataqualitytypecv'
        verbose_name = 'Data Quality Type'


class DataQualityTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'dataqualitytypecvrequests'
        verbose_name = 'Data Quality Type Request'


class RelationshipType(ControlledVocabulary):
    class Meta:
        db_table = 'relationshiptypecv'
        verbose_name = 'Relationship Type'


class RelationshipTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'relationshiptypecvrequests'
        verbose_name = 'Relationship Type Request'


class Medium(ControlledVocabulary):
    class Meta:
        db_table = 'mediumcv'
        verbose_name = 'Medium'


class MediumRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'mediumcvrequests'
        verbose_name = 'Medium Request'
