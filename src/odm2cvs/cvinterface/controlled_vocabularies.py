from cvservices.models import *
from cvinterface.views.base_views import *

vocabulary_list_view = DefaultVocabularyListView
vocabulary_detail_view = DefaultVocabularyDetailView
vocabulary_list_template = 'cvinterface/vocabularies/default_list.html'
vocabulary_detail_template = 'cvinterface/vocabularies/default_detail.html'

request_list_view = DefaultRequestListView
request_create_view = DefaultRequestCreateView
request_update_view = DefaultRequestUpdateView
request_list_template = 'cvinterface/requests/default_list.html'
request_create_template = 'cvinterface/requests/default_form.html'
request_update_template = 'cvinterface/requests/default_update_form.html'

vocabularies = {
    # optional keys:
    # list_view, detail_view, list_template, detail_template

    'actiontype': {
        'name': ActionType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of actions performed in making observations. Depending on the action type, the action may or may not produce an observation result.',
        'model': ActionType,
    },
    'methodtype': {
        'name': MethodType._meta.verbose_name,
        'definition': 'A vocabulary for describing types of Methods associated with creating observations. MethodTypes correspond with ActionTypes in ODM2. An Action must be performed using an appropriate MethodType - e.g., a specimen collection Action should be associated with a specimen collection method.',
        'model': MethodType,
    },
    'aggregationstatistic': {
        'name': AggregationStatistic._meta.verbose_name,
        'definition': 'A vocabulary for describing the calculated statistic associated with recorded observations. The aggregation statistic is calculated over the time aggregation interval associated with the recorded observation. ',
        'model': AggregationStatistic,
    },
    'annotationtype': {
        'name': AnnotationType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of annotation. In ODM2 the annotation type determines whether the annotation forms a grouping of related entities (e.g., a group of sites or variables) or an annotation of a particular entity (e.g., a comment about an individual Site or data value). ',
        'model': AnnotationType,
    },
    'censorcode': {
        'name': CensorCode._meta.verbose_name,
        'definition': 'A vocabulary for describing whether a data value was determined or whether the actual value is unknown due to right or left censoring.',
        'model': CensorCode,
    },
    'datasettype': {
        'name': DatasetType._meta.verbose_name,
        'definition': 'A vocabulary for describing types of Datasets in ODM2. Datasets are logical groupings of Results.',
        'model': DatasetType,
    },
    'directivetype': {
        'name': DirectiveType._meta.verbose_name,
        'definition': 'A vocabulary for describing types of directives under which observations are made. Examples include projects, monitoring programs, campaigns, etc.',
        'model': DirectiveType,
    },
    'elevationdatum': {
        'name': ElevationDatum._meta.verbose_name,
        'definition': 'A vocabulary for describing vertical datums. Vertical datums are used in ODM2 to specify the origin for elevations assocated with SamplingFeatures.',
        'model': ElevationDatum,
    },
    'equipmenttype': {
        'name': EquipmentType._meta.verbose_name,
        'definition': 'A vocabulary for describing types of equipment used for making observations. Examples include sensors, batteries, radios, dataloggers, samplers, etc.',
        'model': EquipmentType,
    },
    'organizationtype': {
        'name': OrganizationType._meta.verbose_name,
        'definition': 'A vocabulary for describing types of Organizations. In ODM2, People may or may not be affiliated with an Organization. People can also be affiliated with more than one Organization.',
        'model': OrganizationType,
    },
    'propertydatatype': {
        'name': PropertyDataType._meta.verbose_name,
        'definition': 'A vocabulary for describing the data type for an extension property in ODM2.  Extension properties can be added to many of the entities in ODM2 (e.g., Sites, Variables, etc.). The values of these extension properties must be of one of the listed primitive data types.',
        'model': PropertyDataType,
    },
    'qualitycode': {
        'name': QualityCode._meta.verbose_name,
        'definition': 'A vocabulary for describing the quality of the observation.',
        'model': QualityCode,
    },
    'resulttype': {
        'name': ResultType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of the Result. In ODM2 Results are separated from, but related to their data values. Each ResultType has a set of related tables for storing the data values for any result of that type.',
        'model': ResultType,
    },
    'samplingfeaturegeotype': {
        'name': SamplingFeatureGeotype._meta.verbose_name,
        'definition': 'A vocabulary for describing the geospatial feature type associated with a SamplingFeature. For example, Site SamplingFeatures are represented as points. In ODM2, each SamplingFeature may have only one geospatial type, but a geospatial types may range from simple points to a complex polygons or even three dimensional volumes.',
        'model': SamplingFeatureGeotype,
    },
    'samplingfeaturetype': {
        'name': SamplingFeatureType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of SamplingFeature. Many different SamplingFeature types can be represented in ODM2. SamplingFeatures of type Site and Specimen will be the most common, but many different types of varying levels of complexity can be used.',
        'model': SamplingFeatureType,
    },
    'sitetype': {
        'name': SiteType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of a data collection Site. To some extent, these types represent the ultimate feature of interest that the site was established to measure. For example, a Stream Site was established to measure properties of a Stream.',
        'model': SiteType,
    },
    'spatialoffsettype': {
        'name': SpatialOffsetType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of SpatialOffset that exists between two SamplingFeatures.',
        'model': SpatialOffsetType,
    },
    'speciation': {
        'name': Speciation._meta.verbose_name,
        'definition': 'A vocabulary for describing the speciation in which a measured variable is expressed.',
        'model': Speciation,
    },
    'specimentype': {
        'name': SpecimenType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of a physical Specimen.',
        'model': SpecimenType,
    },
    'status': {
        'name': Status._meta.verbose_name,
        'definition': 'A vocabulary for describing the data collection status of a Result. In ODM2 the StatusCV can be used to specify whether data collection is planned, ongoing, or complete.',
        'model': Status,
    },
    'taxonomicclassifiertype': {
        'name': TaxonomicClassifierType._meta.verbose_name,
        'definition': 'A vocabulary for describing types of taxonomies from which descriptive terms used in an ODM2 database have been drawn. Taxonomic classifiers provide a way to classify Results and Specimens according to terms from a formal taxonomy.',
        'model': TaxonomicClassifierType,
    },
    'variablename': {
        'name': VariableName._meta.verbose_name,
        'definition': 'A vocabulary for describing the name of Variables.',
        'model': VariableName,
    },
    'variabletype': {
        'name': VariableType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of Variables. VariableTypes provide a way to group Variables into categories for easier querying and filtering.',
        'model': VariableType,
    },
    'dataqualitytype': {
        'name': DataQualityType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of data quality information provided for a particular Result. Examples include the accuracy or precision of the data values within the Result.',
        'model': DataQualityType,
    },
    'relationshiptype': {
        'name': RelationshipType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of relationship between two entities in an ODM2 database. Examples include related Actions, Results, datasets, etc. The RelationshipType describes the nature of the relationship between the two entity instances (e.g., a Specimen SamplingFeature "was collected at" a Site SamplingFeature).',
        'model': RelationshipType,
    },
    'medium': {
        'name': Medium._meta.verbose_name,
        'definition': 'A vocabulary for describing the physical medium of a specimen, reference material, or sampled environment.',
        'model': Medium,
    },
    'unitstype': {
        'name': UnitsType._meta.verbose_name,
        'definition': 'A vocabulary for describing the type of the Unit or the more general quantity that the Unit represents.',
        'model': UnitsType,
    },
}

requests = {
    # optional keys:
    # list_view, create_view, update_view, list_template, create_template, update_template

    'actiontyperequest': {
        'vocabulary': 'actiontype',
        'vocabulary_model': ActionType,
        'name': ActionTypeRequest._meta.verbose_name,
        'model': ActionTypeRequest,
    },
    'methodtyperequest': {
        'vocabulary': 'methodtype',
        'vocabulary_model': MethodType,
        'name': MethodTypeRequest._meta.verbose_name,
        'model': MethodTypeRequest,
    },
    'aggregationstatisticrequest': {
        'vocabulary': 'aggregationstatistic',
        'vocabulary_model': AggregationStatistic,
        'name': AggregationStatisticRequest._meta.verbose_name,
        'model': AggregationStatisticRequest,
    },
    'annotationtyperequest': {
        'vocabulary': 'annotationtype',
        'vocabulary_model': AnnotationType,
        'name': AnnotationTypeRequest._meta.verbose_name,
        'model': AnnotationTypeRequest,
    },
    'censorcoderequest': {
        'vocabulary': 'censorcode',
        'vocabulary_model': CensorCode,
        'name': CensorCodeRequest._meta.verbose_name,
        'model': CensorCodeRequest,
    },
    'datasettyperequest': {
        'vocabulary': 'datasettype',
        'vocabulary_model': DatasetType,
        'name': DatasetTypeRequest._meta.verbose_name,
        'model': DatasetTypeRequest,
    },
    'directivetyperequest': {
        'vocabulary': 'directivetype',
        'vocabulary_model': DirectiveType,
        'name': DirectiveTypeRequest._meta.verbose_name,
        'model': DirectiveTypeRequest,
    },
    'elevationdatumrequest': {
        'vocabulary': 'elevationdatum',
        'vocabulary_model': ElevationDatum,
        'name': ElevationDatumRequest._meta.verbose_name,
        'model': ElevationDatumRequest,
    },
    'equipmenttyperequest': {
        'vocabulary': 'equipmenttype',
        'vocabulary_model': EquipmentType,
        'name': EquipmentTypeRequest._meta.verbose_name,
        'model': EquipmentTypeRequest,
    },
    'organizationtyperequest': {
        'vocabulary': 'organizationtype',
        'vocabulary_model': OrganizationType,
        'name': OrganizationTypeRequest._meta.verbose_name,
        'model': OrganizationTypeRequest,
    },
    'propertydatatyperequest': {
        'vocabulary': 'propertydatatype',
        'vocabulary_model': PropertyDataType,
        'name': PropertyDataTypeRequest._meta.verbose_name,
        'model': PropertyDataTypeRequest,
    },
    'qualitycoderequest': {
        'vocabulary': 'qualitycode',
        'vocabulary_model': QualityCode,
        'name': QualityCodeRequest._meta.verbose_name,
        'model': QualityCodeRequest,
    },
    'resulttyperequest': {
        'vocabulary': 'resulttype',
        'vocabulary_model': ResultType,
        'name': ResultTypeRequest._meta.verbose_name,
        'model': ResultTypeRequest,
    },
    'samplingfeaturegeotyperequest': {
        'vocabulary': 'samplingfeaturegeotype',
        'vocabulary_model': SamplingFeatureGeotype,
        'name': SamplingFeatureGeotypeRequest._meta.verbose_name,
        'model': SamplingFeatureGeotypeRequest,
    },
    'samplingfeaturetyperequest': {
        'vocabulary': 'samplingfeaturetype',
        'vocabulary_model': SamplingFeatureType,
        'name': SamplingFeatureTypeRequest._meta.verbose_name,
        'model': SamplingFeatureTypeRequest,
    },
    'sitetyperequest': {
        'vocabulary': 'sitetype',
        'vocabulary_model': SiteType,
        'name': SiteTypeRequest._meta.verbose_name,
        'model': SiteTypeRequest,
    },
    'spatialoffsettyperequest': {
        'vocabulary': 'spatialoffsettype',
        'vocabulary_model': SpatialOffsetType,
        'name': SpatialOffsetTypeRequest._meta.verbose_name,
        'model': SpatialOffsetTypeRequest,
    },
    'speciationrequest': {
        'vocabulary': 'speciation',
        'vocabulary_model': Speciation,
        'name': SpeciationRequest._meta.verbose_name,
        'model': SpeciationRequest,
    },
    'specimentyperequest': {
        'vocabulary': 'specimentype',
        'vocabulary_model': SpecimenType,
        'name': SpecimenTypeRequest._meta.verbose_name,
        'model': SpecimenTypeRequest,
    },
    'statusrequest': {
        'vocabulary': 'status',
        'vocabulary_model': Status,
        'name': StatusRequest._meta.verbose_name,
        'model': StatusRequest,
    },
    'taxonomicclassifiertyperequest': {
        'vocabulary': 'taxonomicclassifiertype',
        'vocabulary_model': TaxonomicClassifierType,
        'name': TaxonomicClassifierTypeRequest._meta.verbose_name,
        'model': TaxonomicClassifierTypeRequest,
    },
    'variablenamerequest': {
        'vocabulary': 'variablename',
        'vocabulary_model': VariableName,
        'name': VariableNameRequest._meta.verbose_name,
        'model': VariableNameRequest,
    },
    'variabletyperequest': {
        'vocabulary': 'variabletype',
        'vocabulary_model': VariableType,
        'name': VariableTypeRequest._meta.verbose_name,
        'model': VariableTypeRequest,
    },
    'dataqualitytyperequest': {
        'vocabulary': 'dataqualitytype',
        'vocabulary_model': DataQualityType,
        'name': DataQualityTypeRequest._meta.verbose_name,
        'model': DataQualityTypeRequest,
    },
    'relationshiptyperequest': {
        'vocabulary': 'relationshiptype',
        'vocabulary_model': RelationshipType,
        'name': RelationshipTypeRequest._meta.verbose_name,
        'model': RelationshipTypeRequest,
    },
    'mediumrequest': {
        'vocabulary': 'medium',
        'vocabulary_model': Medium,
        'name': MediumRequest._meta.verbose_name,
        'model': MediumRequest,
    },
    'unitstyperequest': {
        'vocabulary': 'unitstype',
        'vocabulary_model': UnitsType,
        'name': UnitsTypeRequest._meta.verbose_name,
        'model': UnitsTypeRequest,
    },
}
