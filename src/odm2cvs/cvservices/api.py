from tastypie.api import Api

from rdfserializer.api import ModelRdfResource
from models import ActionType, MethodType, OrganizationType, SamplingFeatureGeotype, SamplingFeatureType, SiteType, \
    AggregationStatistic, AnnotationType, CensorCode, DatasetType, DirectiveType, ElevationDatum, EquipmentType, \
    PropertyDataType, QualityCode, Medium, ResultType, SpatialOffsetType, UnitsType, Speciation, Status, \
    TaxonomicClassifierType, VariableName, VariableType, SpecimenType, DataQualityType, RelationshipType


class UnitsTypeResource(ModelRdfResource):
    scheme = 'unitsType'

    class Meta(ModelRdfResource.Meta):
        queryset = UnitsType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'unitstype'


class ActionTypeResource(ModelRdfResource):
    scheme = 'actionType'

    class Meta(ModelRdfResource.Meta):
        queryset = ActionType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'actiontype'


class MethodTypeResource(ModelRdfResource):
    scheme = 'methodType'

    class Meta(ModelRdfResource.Meta):
        queryset = MethodType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'methodtype'


class OrganizationTypeResource(ModelRdfResource):
    scheme = 'organizationType'

    class Meta(ModelRdfResource.Meta):
        queryset = OrganizationType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'organizationtype'


class SamplingFeatureGeotypeResource(ModelRdfResource):
    scheme = 'samplingFeatureGeotype'

    class Meta(ModelRdfResource.Meta):
        queryset = SamplingFeatureGeotype.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'samplingfeaturegeotype'


class SamplingFeatureTypeResource(ModelRdfResource):
    scheme = 'samplingFeatureType'

    class Meta(ModelRdfResource.Meta):
        queryset = SamplingFeatureType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'samplingfeaturetype'


class SiteTypeResource(ModelRdfResource):
    scheme = 'siteType'

    class Meta(ModelRdfResource.Meta):
        queryset = SiteType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'sitetype'


class AggregationStatisticResource(ModelRdfResource):
    scheme = 'aggregationStatistic'

    class Meta(ModelRdfResource.Meta):
        queryset = AggregationStatistic.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'aggregationstatistic'


class AnnotationTypeResource(ModelRdfResource):
    scheme = 'annotationType'

    class Meta(ModelRdfResource.Meta):
        queryset = AnnotationType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'annotationtype'


class CensorCodeResource(ModelRdfResource):
    scheme = 'censorCode'

    class Meta(ModelRdfResource.Meta):
        queryset = CensorCode.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'censorcode'


class DatasetTypeResource(ModelRdfResource):
    scheme = 'datasetType'

    class Meta(ModelRdfResource.Meta):
        queryset = DatasetType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'datasettype'


class DirectiveTypeResource(ModelRdfResource):
    scheme = 'directiveType'

    class Meta(ModelRdfResource.Meta):
        queryset = DirectiveType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'directivetype'


class ElevationDatumResource(ModelRdfResource):
    scheme = 'elevationDatum'

    class Meta(ModelRdfResource.Meta):
        queryset = ElevationDatum.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'elevationdatum'


class EquipmentTypeResource(ModelRdfResource):
    scheme = 'equipmentType'

    class Meta(ModelRdfResource.Meta):
        queryset = EquipmentType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'equipmenttype'


class PropertyDataTypeResource(ModelRdfResource):
    scheme = 'propertyDataType'

    class Meta(ModelRdfResource.Meta):
        queryset = PropertyDataType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'propertydatatype'


class QualityCodeResource(ModelRdfResource):
    scheme = 'qualityCode'

    class Meta(ModelRdfResource.Meta):
        queryset = QualityCode.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'qualitycode'


class ResultTypeResource(ModelRdfResource):
    scheme = 'resultType'

    class Meta(ModelRdfResource.Meta):
        queryset = ResultType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'resulttype'


class SpatialOffsetTypeResource(ModelRdfResource):
    scheme = 'spatialOffsetType'

    class Meta(ModelRdfResource.Meta):
        queryset = SpatialOffsetType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'spatialoffsettype'


class SpeciationResource(ModelRdfResource):
    scheme = 'speciation'

    class Meta(ModelRdfResource.Meta):
        queryset = Speciation.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'speciation'


class SpecimenTypeResource(ModelRdfResource):
    scheme = 'specimenType'

    class Meta(ModelRdfResource.Meta):
        queryset = SpecimenType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'specimentype'


class StatusResource(ModelRdfResource):
    scheme = 'status'

    class Meta(ModelRdfResource.Meta):
        queryset = Status.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'status'


class TaxonomicClassifierTypeResource(ModelRdfResource):
    scheme = 'taxonomicClassifierType'

    class Meta(ModelRdfResource.Meta):
        queryset = TaxonomicClassifierType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'taxonomicclassifiertype'


class VariableNameResource(ModelRdfResource):
    scheme = 'variableName'

    class Meta(ModelRdfResource.Meta):
        queryset = VariableName.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'variablename'


class VariableTypeResource(ModelRdfResource):
    scheme = 'variableType'

    class Meta(ModelRdfResource.Meta):
        queryset = VariableType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'variabletype'


class DataQualityTypeResource(ModelRdfResource):
    scheme = 'dataQualityType'

    class Meta(ModelRdfResource.Meta):
        queryset = DataQualityType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'dataqualitytype'


class RelationshipTypeResource(ModelRdfResource):
    scheme = 'relationshipType'

    class Meta(ModelRdfResource.Meta):
        queryset = RelationshipType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'relationshiptype'


class MediumResource(ModelRdfResource):
    scheme = 'medium'

    class Meta(ModelRdfResource.Meta):
        queryset = Medium.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'medium'


v1_api = Api(api_name='v1')
v1_api.register(ActionTypeResource())
v1_api.register(MethodTypeResource())
v1_api.register(OrganizationTypeResource())
v1_api.register(SamplingFeatureGeotypeResource())
v1_api.register(SamplingFeatureTypeResource())
v1_api.register(SiteTypeResource())
v1_api.register(AggregationStatisticResource())
v1_api.register(AnnotationTypeResource())
v1_api.register(CensorCodeResource())
v1_api.register(DatasetTypeResource())
v1_api.register(DirectiveTypeResource())
v1_api.register(ElevationDatumResource())
v1_api.register(EquipmentTypeResource())
v1_api.register(PropertyDataTypeResource())
v1_api.register(QualityCodeResource())
v1_api.register(ResultTypeResource())
v1_api.register(SpatialOffsetTypeResource())
v1_api.register(SpeciationResource())
v1_api.register(SpecimenTypeResource())
v1_api.register(StatusResource())
v1_api.register(TaxonomicClassifierTypeResource())
v1_api.register(VariableNameResource())
v1_api.register(VariableTypeResource())
v1_api.register(DataQualityTypeResource())
v1_api.register(RelationshipTypeResource())
v1_api.register(MediumResource())
v1_api.register(UnitsTypeResource())
