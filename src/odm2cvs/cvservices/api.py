import csv
from collections import OrderedDict
from io import StringIO

from tastypie.api import Api
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from models import ActionType, AggregationStatistic, AnnotationType, CensorCode, DataQualityType, DatasetType, \
    DirectiveType, ElevationDatum, EquipmentType, Medium, MethodType, OrganizationType, PropertyDataType, QualityCode, \
    RelationshipType, ResultType, SamplingFeatureGeotype, SamplingFeatureType, SiteType, SpatialOffsetType, Speciation, \
    SpecimenType, Status, TaxonomicClassifierType, UnitsType, VariableName, VariableType, Unit

from src.odm2cvs.rdfserializer.api import ModelRdfResource


class CSVSerializer(Serializer):
    formats = ['csv']
    content_types = {
        'csv': 'text/plain'
    }

    def to_csv(self, data, options=None, writer=None):
        options = options or {}
        data = self.to_simple(data, options)
        excluded_fields = [u'resource_uri']

        raw_data = StringIO()
        first = True

        if "meta" in data.keys():
            objects = data.get("objects")

            for value in objects:
                test = {}
                for excluded_field in excluded_fields:
                    del value[excluded_field]
                self.flatten(value, test)

                odict = OrderedDict()
                odict['Term'] = test['term']
                del test['term']
                odict['UnitsName'] = test['name']
                del test['name']
                odict['UnitsTypeCV'] = test['type']
                del test['type']
                odict['UnitsAbbreviation'] = test['abbreviation']
                del test['abbreviation']
                odict['UnitsLink'] = test['link']
                del test['link']

                if first:
                    writer = csv.DictWriter(raw_data, odict.keys())
                    writer.writeheader()
                    writer.writerow(odict)
                    first = False
                else:
                    writer.writerow({k: (v.encode('utf-8') if isinstance(v, int) is not True and isinstance(v, type(
                        None)) is not True else v) for k, v in odict.items()})
        else:
            test = {}
            for excluded_field in excluded_fields:
                del data[excluded_field]
            self.flatten(data, test)
            odict = OrderedDict()
            odict['Term'] = test['term']
            del test['term']
            odict['UnitsName'] = test['name']
            del test['name']
            odict['UnitsTypeCV'] = test['type']
            del test['type']
            odict['UnitsAbbreviation'] = test['abbreviation']
            del test['abbreviation']
            odict['UnitsLink'] = test['link']
            del test['link']

            if first:
                writer = csv.DictWriter(raw_data, odict.keys())
                writer.writeheader()
                writer.writerow(odict)
                first = False
            else:
                writer.writerow(odict)
        CSVContent = raw_data.getvalue()
        return CSVContent

    def flatten(self, data, odict={}):
        if isinstance(data, list):
            for value in data:
                self.flatten(value, odict)
        elif isinstance(data, dict):
            for (key, value) in data.items():
                if not isinstance(value, (dict, list)):
                    odict[key] = value
                else:
                    self.flatten(value, odict)


class UnitsResource(ModelResource):
    class Meta:
        queryset = Unit.objects.all()
        serializer = CSVSerializer()
        allowed_methods = ['get']
        resource_name = 'units'
        excludes = ['unit_id']


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
v1_api.register(UnitsResource())
