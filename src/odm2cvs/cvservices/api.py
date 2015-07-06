from tastypie.api import Api
from tastypie.resources import ModelResource

from rdfserializer.api import RdfSerializer, ModelRdfResource
from models import ActionType, ActionTypeRequest, MethodType, MethodTypeRequest, \
    OrganizationType, OrganizationTypeRequest, SamplingFeatureGeotype, SamplingFeatureGeotypeRequest, \
    SamplingFeatureType, SamplingFeatureTypeRequest, SiteType, SiteTypeRequest, AggregationStatistic, \
    AggregationStatisticRequest, AnnotationType, AnnotationTypeRequest, CensorCode, \
    CensorCodeRequest, DatasetType, DatasetTypeRequest, DirectiveType, DirectiveTypeRequest, \
    ElevationDatum, ElevationDatumRequest, EquipmentType, EquipmentTypeRequest, PropertyDataType, PropertyDataTypeRequest, \
    QualityCode, QualityCodeRequest, Medium, MediumRequest,\
    ResultType, ResultTypeRequest, SpatialOffsetType, UnitsType, UnitsTypeRequest, \
    SpatialOffsetTypeRequest, Speciation, SpeciationRequest, Status, StatusRequest, \
    TaxonomicClassifierType, TaxonomicClassifierTypeRequest, VariableName, VariableNameRequest, \
    VariableType, VariableTypeRequest, SpecimenType, \
    SpecimenTypeRequest, DataQualityType, DataQualityTypeRequest, RelationshipType, RelationshipTypeRequest

class UnitsTypeResource(ModelRdfResource):
    scheme = 'unitsType'

    class Meta:
        queryset = UnitsType.objects.using('control_vocabularies').all()
        resource_name = 'unitstype'
        max_limit = 0
        serializer = RdfSerializer()

class UnitsTypeRequestResource(ModelResource):
    class Meta:
        queryset = UnitsTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'unitstyperequest'
        max_limit = 0


class ActionTypeResource(ModelRdfResource):
    scheme = 'actionType'

    class Meta:
        queryset = ActionType.objects.using('control_vocabularies').all()
        resource_name = 'actiontype'
        max_limit = 0
        serializer = RdfSerializer()


class ActionTypeRequestResource(ModelResource):
    class Meta:
        queryset = ActionTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'actiontyperequest'
        max_limit = 0


class MethodTypeResource(ModelRdfResource):
    scheme = 'methodType'

    class Meta:
        queryset = MethodType.objects.using('control_vocabularies').all()
        resource_name = 'methodtype'
        max_limit = 0
        serializer = RdfSerializer()

class MethodTypeRequestResource(ModelResource):
    class Meta:
        queryset = MethodTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'methodtyperequest'
        max_limit = 0

class OrganizationTypeResource(ModelRdfResource):
    scheme = 'organizationType'

    class Meta:
        queryset = OrganizationType.objects.using('control_vocabularies').all()
        resource_name = 'organizationtype'
        max_limit = 0
        serializer = RdfSerializer()


class OrganizationTypeRequestResource(ModelResource):
    class Meta:
        queryset = OrganizationTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'organizationtyperequest'
        max_limit = 0


class SamplingFeatureGeotypeResource(ModelRdfResource):
    scheme = 'samplingFeatureGeotype'

    class Meta:
        queryset = SamplingFeatureGeotype.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturegeotype'
        max_limit = 0
        serializer = RdfSerializer()


class SamplingFeatureGeotypeRequestResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureGeotypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturegeotyperequest'
        max_limit = 0


class SamplingFeatureTypeResource(ModelRdfResource):
    scheme = 'samplingFeatureType'

    class Meta:
        queryset = SamplingFeatureType.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturetype'
        max_limit = 0
        serializer = RdfSerializer()


class SamplingFeatureTypeRequestResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturetyperequest'
        max_limit = 0


class SiteTypeResource(ModelRdfResource):
    scheme = 'siteType'

    class Meta:
        queryset = SiteType.objects.using('control_vocabularies').all()
        resource_name = 'sitetype'
        max_limit = 0
        serializer = RdfSerializer()


class SiteTypeRequestResource(ModelResource):
    class Meta:
        queryset = SiteTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'sitetyperequests'
        max_limit = 0

# Denver
class AggregationStatisticResource(ModelRdfResource):
    scheme = 'aggregationStatistic'

    class Meta:
        queryset = AggregationStatistic.objects.using('control_vocabularies').all()
        resource_name = 'aggregationstatistic'
        max_limit = 0
        serializer = RdfSerializer()


class AggregationStatisticRequestResource(ModelResource):
    class Meta:
        queryset = AggregationStatisticRequest.objects.using('control_vocabularies').all()
        resource_name = 'aggregationstatisticrequest'
        max_limit = 0


class AnnotationTypeResource(ModelRdfResource):
    scheme = 'annotationType'

    class Meta:
        queryset = AnnotationType.objects.using('control_vocabularies').all()
        resource_name = 'annotationtype'
        max_limit = 0
        serializer = RdfSerializer()


class AnnotationTypeRequestResource(ModelResource):
    class Meta:
        queryset = AnnotationTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'annotationtyperequest'
        max_limit = 0


class CensorCodeResource(ModelRdfResource):
    scheme = 'censorCode'

    class Meta:
        queryset = CensorCode.objects.using('control_vocabularies').all()
        resource_name = 'censorcode'
        max_limit = 0
        serializer = RdfSerializer()


class CensorCodeRequestResource(ModelResource):
    class Meta:
        queryset = CensorCodeRequest.objects.using('control_vocabularies').all()
        resource_name = 'censorcoderequest'
        max_limit = 0


class DatasetTypeResource(ModelRdfResource):
    scheme = 'datasetType'

    class Meta:
        queryset = DatasetType.objects.using('control_vocabularies').all()
        resource_name = 'datasettype'
        max_limit = 0
        serializer = RdfSerializer()


class DatasetTypeRequestResource(ModelResource):
    class Meta:
        queryset = DatasetTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'datasettyperequest'
        max_limit = 0


class DirectiveTypeResource(ModelRdfResource):
    scheme = 'directiveType'

    class Meta:
        queryset = DirectiveType.objects.using('control_vocabularies').all()
        resource_name = 'directivetype'
        max_limit = 0
        serializer = RdfSerializer()


class DirectiveTypeRequestResource(ModelResource):
    class Meta:
        queryset = DirectiveTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'directivetyperequest'
        max_limit = 0


class ElevationDatumResource(ModelRdfResource):
    scheme = 'elevationDatum'

    class Meta:
        queryset = ElevationDatum.objects.using('control_vocabularies').all()
        resource_name = 'elevationdatum'
        max_limit = 0
        serializer = RdfSerializer()


class ElevationDatumRequestResource(ModelResource):
    class Meta:
        queryset = ElevationDatumRequest.objects.using('control_vocabularies').all()
        resource_name = 'elevationdatumrequest'
        max_limit = 0


class EquipmentTypeResource(ModelRdfResource):
    scheme = 'equipmentType'

    class Meta:
        queryset = EquipmentType.objects.using('control_vocabularies').all()
        resource_name = 'equipmenttype'
        max_limit = 0
        serializer = RdfSerializer()


class EquipmentTypeRequestResource(ModelResource):
    class Meta:
        queryset = EquipmentTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'equipmenttyperequest'
        max_limit = 0


class PropertyDataTypeResource(ModelRdfResource):
    scheme = 'propertyDataType'

    class Meta:
        queryset = PropertyDataType.objects.using('control_vocabularies').all()
        resource_name = 'propertydatatype'
        max_limit = 0
        serializer = RdfSerializer()


class PropertyDataTypeRequestResource(ModelResource):
    class Meta:
        queryset = PropertyDataTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'propertydatatyperequest'
        max_limit = 0


class QualityCodeResource(ModelRdfResource):
    scheme = 'qualityCode'

    class Meta:
        queryset = QualityCode.objects.using('control_vocabularies').all()
        resource_name = 'qualitycode'
        max_limit = 0
        serializer = RdfSerializer()


class QualityCodeRequestResource(ModelResource):
    class Meta:
        queryset = QualityCodeRequest.objects.using('control_vocabularies').all()
        resource_name = 'qualitycoderequest'
        max_limit = 0


class ResultTypeResource(ModelRdfResource):
    scheme = 'resultType'

    class Meta:
        queryset = ResultType.objects.using('control_vocabularies').all()
        resource_name = 'resulttype'
        max_limit = 0
        serializer = RdfSerializer()


class ResultTypeRequestResource(ModelResource):
    class Meta:
        queryset = ResultTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'resulttyperequest'
        max_limit = 0


class SpatialOffsetTypeResource(ModelRdfResource):
    scheme = 'spatialOffsetType'

    class Meta:
        queryset = SpatialOffsetType.objects.using('control_vocabularies').all()
        resource_name = 'spatialoffsettype'
        max_limit = 0
        serializer = RdfSerializer()


class SpatialOffsetTypeRequestResource(ModelResource):
    class Meta:
        queryset = SpatialOffsetTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'spatialoffsettyperequest'
        max_limit = 0


class SpeciationResource(ModelRdfResource):
    scheme = 'speciation'

    class Meta:
        queryset = Speciation.objects.using('control_vocabularies').all()
        resource_name = 'speciation'
        max_limit = 0
        serializer = RdfSerializer()


class SpeciationRequestResource(ModelResource):
    class Meta:
        queryset = SpeciationRequest.objects.using('control_vocabularies').all()
        resource_name = 'speciationrequest'
        max_limit = 0


class SpecimenTypeResource(ModelRdfResource):
    scheme = 'specimenType'

    class Meta:
        queryset = SpecimenType.objects.using('control_vocabularies').all()
        resource_name = 'specimentype'
        max_limit = 0
        serializer = RdfSerializer()


class SpecimenTypeRequestResource(ModelResource):
    class Meta:
        queryset = SpecimenTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'specimentyperequest'
        max_limit = 0


class StatusResource(ModelRdfResource):
    scheme = 'status'

    class Meta:
        queryset = Status.objects.using('control_vocabularies').all()
        resource_name = 'status'
        max_limit = 0
        serializer = RdfSerializer()


class StatusRequestResource(ModelResource):
    class Meta:
        queryset = StatusRequest.objects.using('control_vocabularies').all()
        resource_name = 'statusrequest'
        max_limit = 0


class TaxonomicClassifierTypeResource(ModelRdfResource):
    scheme = 'taxonomicClassifierType'

    class Meta:
        queryset = TaxonomicClassifierType.objects.using('control_vocabularies').all()
        resource_name = 'taxonomicclassifiertype'
        max_limit = 0
        serializer = RdfSerializer()


class TaxonomicClassifierTypeRequestResource(ModelResource):
    class Meta:
        queryset = TaxonomicClassifierTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'taxonomicclassifiertyperequest'
        max_limit = 0


class VariableNameResource(ModelRdfResource):
    scheme = 'variableName'

    class Meta:
        queryset = VariableName.objects.using('control_vocabularies').all()
        resource_name = 'variablename'
        max_limit = 0
        serializer = RdfSerializer()


class VariableNameRequestResource(ModelResource):
    class Meta:
        queryset = VariableNameRequest.objects.using('control_vocabularies').all()
        resource_name = 'variablenamerequest'
        max_limit = 0


class VariableTypeResource(ModelRdfResource):
    scheme = 'variableType'

    class Meta:
        queryset = VariableType.objects.using('control_vocabularies').all()
        resource_name = 'variabletype'
        max_limit = 0
        serializer = RdfSerializer()


class VariableTypeRequestResource(ModelResource):
    class Meta:
        queryset = VariableTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'variabletyperequest'
        max_limit = 0

class DataQualityTypeResource(ModelRdfResource):
    scheme = 'dataQualityType'

    class Meta:
        queryset = DataQualityType.objects.using('control_vocabularies').all()
        resource_name = 'dataqualitytype'
        max_limit = 0
        serializer = RdfSerializer()


class DataQualityTypeRequestResource(ModelResource):
    class Meta:
        queryset = DataQualityTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'dataqualitytyperequest'
        max_limit = 0

class RelationshipTypeResource(ModelRdfResource):
    scheme = 'relationshipType'

    class Meta:
        queryset = RelationshipType.objects.using('control_vocabularies').all()
        resource_name = 'relationshiptype'
        max_limit = 0
        serializer = RdfSerializer()


class RelationshipTypeRequestResource(ModelResource):
    class Meta:
        queryset = RelationshipTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'relationshiptyperequest'
        max_limit = 0

class MediumResource(ModelRdfResource):
    scheme = 'medium'

    class Meta:
        queryset = Medium.objects.using('control_vocabularies').all()
        resource_name = 'medium'
        max_limit = 0
        serializer = RdfSerializer()

class MediumRequestResource(ModelResource):
    class Meta:
        queryset = MediumRequest.objects.using('control_vocabularies').all()
        resource_name = 'mediumrequest'
        max_limit = 0

v1_api = Api(api_name='v1')
v1_api.register(ActionTypeResource())
v1_api.register(ActionTypeRequestResource())
v1_api.register(MethodTypeResource())
v1_api.register(MethodTypeRequestResource())
v1_api.register(OrganizationTypeResource())
v1_api.register(OrganizationTypeRequestResource())
v1_api.register(SamplingFeatureGeotypeResource())
v1_api.register(SamplingFeatureGeotypeRequestResource())
v1_api.register(SamplingFeatureTypeResource())
v1_api.register(SamplingFeatureTypeRequestResource())
v1_api.register(SiteTypeResource())
v1_api.register(SiteTypeRequestResource())
v1_api.register(AggregationStatisticResource())
v1_api.register(AggregationStatisticRequestResource())
v1_api.register(AnnotationTypeResource())
v1_api.register(AnnotationTypeRequestResource())
v1_api.register(CensorCodeResource())
v1_api.register(CensorCodeRequestResource())
v1_api.register(DatasetTypeResource())
v1_api.register(DatasetTypeRequestResource())
v1_api.register(DirectiveTypeResource())
v1_api.register(DirectiveTypeRequestResource())
v1_api.register(ElevationDatumResource())
v1_api.register(ElevationDatumRequestResource())
v1_api.register(EquipmentTypeResource())
v1_api.register(EquipmentTypeRequestResource())
v1_api.register(PropertyDataTypeResource())
v1_api.register(PropertyDataTypeRequestResource())
v1_api.register(QualityCodeResource())
v1_api.register(QualityCodeRequestResource())
v1_api.register(ResultTypeResource())
v1_api.register(ResultTypeRequestResource())
v1_api.register(SpatialOffsetTypeResource())
v1_api.register(SpatialOffsetTypeRequestResource())
v1_api.register(SpeciationResource())
v1_api.register(SpeciationRequestResource())
v1_api.register(SpecimenTypeResource())
v1_api.register(SpecimenTypeRequestResource())
v1_api.register(StatusResource())
v1_api.register(StatusRequestResource())
v1_api.register(TaxonomicClassifierTypeResource())
v1_api.register(TaxonomicClassifierTypeRequestResource())
v1_api.register(VariableNameResource())
v1_api.register(VariableNameRequestResource())
v1_api.register(VariableTypeResource())
v1_api.register(VariableTypeRequestResource())
v1_api.register(DataQualityTypeResource())
v1_api.register(DataQualityTypeRequestResource())
v1_api.register(RelationshipTypeResource())
v1_api.register(RelationshipTypeRequestResource())
v1_api.register(MediumResource())
v1_api.register(MediumRequestResource())
v1_api.register(UnitsTypeResource())
v1_api.register(UnitsTypeRequestResource())
