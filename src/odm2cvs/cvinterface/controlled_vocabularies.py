from src.odm2cvs.cvservices import models as cvmodels
from src.odm2cvs.cvinterface.views import base_views

# TODO: (Pabitra) why are these defined here?

vocabulary_list_view = base_views.DefaultVocabularyListView
vocabulary_detail_view = base_views.DefaultVocabularyDetailView
vocabulary_list_template = 'cvinterface/vocabularies/default_list.html'
vocabulary_detail_template = 'cvinterface/vocabularies/default_detail.html'

request_list_view = base_views.DefaultRequestListView
request_create_view = base_views.DefaultRequestCreateView
request_update_view = base_views.DefaultRequestUpdateView
request_list_template = 'cvinterface/requests/default_list.html'
request_create_template = 'cvinterface/requests/default_form.html'
request_update_template = 'cvinterface/requests/default_update_form.html'


def _get_vocabulary(model, definition):
    return {
        'name': model._meta.verbose_name,
        'definition': definition,
        'model': model,
    }


def _get_request(model, vocabulary, vocabulary_model):
    return {
        'vocabulary': vocabulary,
        'vocabulary_model': vocabulary_model,
        'name': model._meta.verbose_name,
        'model': model,
    }


vocabularies = {
    # optional keys:
    # list_view, detail_view, list_template, detail_template

    'actiontype': _get_vocabulary(cvmodels.ActionType, 'A vocabulary for describing the type of actions performed in making observations. Depending on the action type, the action may or may not produce an observation result.'),
    'methodtype': _get_vocabulary(cvmodels.MethodType, 'A vocabulary for describing types of Methods associated with creating observations. MethodTypes correspond with ActionTypes in ODM2. An Action must be performed using an appropriate MethodType - e.g., a specimen collection Action should be associated with a specimen collection method.'),
    'aggregationstatistic': _get_vocabulary(cvmodels.AggregationStatistic, 'A vocabulary for describing the calculated statistic associated with recorded observations. The aggregation statistic is calculated over the time aggregation interval associated with the recorded observation. '),
    'annotationtype': _get_vocabulary(cvmodels.AnnotationType, 'A vocabulary for describing the type of annotation. In ODM2 the annotation type determines whether the annotation forms a grouping of related entities (e.g., a group of sites or variables) or an annotation of a particular entity (e.g., a comment about an individual Site or data value). '),
    'censorcode': _get_vocabulary(cvmodels.CensorCode, 'A vocabulary for describing whether a data value was determined or whether the actual value is unknown due to right or left censoring.'),
    'datasettype': _get_vocabulary(cvmodels.DatasetType, 'A vocabulary for describing types of Datasets in ODM2. Datasets are logical groupings of Results.'),
    'directivetype': _get_vocabulary(cvmodels.DirectiveType, 'A vocabulary for describing types of directives under which observations are made. Examples include projects, monitoring programs, campaigns, etc.'),
    'elevationdatum': _get_vocabulary(cvmodels.ElevationDatum, 'A vocabulary for describing vertical datums. Vertical datums are used in ODM2 to specify the origin for elevations assocated with SamplingFeatures.'),
    'equipmenttype': _get_vocabulary(cvmodels.EquipmentType, 'A vocabulary for describing types of equipment used for making observations. Examples include sensors, batteries, radios, dataloggers, samplers, etc.'),
    'organizationtype': _get_vocabulary(cvmodels.OrganizationType, 'A vocabulary for describing types of Organizations. In ODM2, People may or may not be affiliated with an Organization. People can also be affiliated with more than one Organization.'),
    'propertydatatype': _get_vocabulary(cvmodels.PropertyDataType, 'A vocabulary for describing the data type for an extension property in ODM2.  Extension properties can be added to many of the entities in ODM2 (e.g., Sites, Variables, etc.). The values of these extension properties must be of one of the listed primitive data types.'),
    'qualitycode': _get_vocabulary(cvmodels.QualityCode, 'A vocabulary for describing the quality of the observation.'),
    'resulttype': _get_vocabulary(cvmodels.ResultType, 'A vocabulary for describing the type of the Result. In ODM2 Results are separated from, but related to their data values. Each ResultType has a set of related tables for storing the data values for any result of that type.'),
    'samplingfeaturegeotype': _get_vocabulary(cvmodels.SamplingFeatureGeotype, 'A vocabulary for describing the geospatial feature type associated with a SamplingFeature. For example, Site SamplingFeatures are represented as points. In ODM2, each SamplingFeature may have only one geospatial type, but a geospatial types may range from simple points to a complex polygons or even three dimensional volumes.'),
    'samplingfeaturetype': _get_vocabulary(cvmodels.SamplingFeatureType, 'A vocabulary for describing the type of SamplingFeature. Many different SamplingFeature types can be represented in ODM2. SamplingFeatures of type Site and Specimen will be the most common, but many different types of varying levels of complexity can be used.'),
    'sitetype': _get_vocabulary(cvmodels.SiteType, 'A vocabulary for describing the type of a data collection Site. To some extent, these types represent the ultimate feature of interest that the site was established to measure. For example, a Stream Site was established to measure properties of a Stream.'),
    'spatialoffsettype': _get_vocabulary(cvmodels.SpatialOffsetType, 'A vocabulary for describing the type of SpatialOffset that exists between two SamplingFeatures.'),
    'speciation': _get_vocabulary(cvmodels.Speciation, 'A vocabulary for describing the speciation in which a measured variable is expressed.'),
    'specimentype': _get_vocabulary(cvmodels.SpecimenType, 'A vocabulary for describing the type of a physical Specimen.'),
    'status': _get_vocabulary(cvmodels.Status, 'A vocabulary for describing the data collection status of a Result. In ODM2 the StatusCV can be used to specify whether data collection is planned, ongoing, or complete.'),
    'taxonomicclassifiertype': _get_vocabulary(cvmodels.TaxonomicClassifierType, 'A vocabulary for describing types of taxonomies from which descriptive terms used in an ODM2 database have been drawn. Taxonomic classifiers provide a way to classify Results and Specimens according to terms from a formal taxonomy.'),
    'variablename': _get_vocabulary(cvmodels.VariableName, 'A vocabulary for describing the name of Variables.'),
    'variabletype': _get_vocabulary(cvmodels.VariableType, 'A vocabulary for describing the type of Variables. VariableTypes provide a way to group Variables into categories for easier querying and filtering.'),
    'dataqualitytype': _get_vocabulary(cvmodels.DataQualityType, 'A vocabulary for describing the type of data quality information provided for a particular Result. Examples include the accuracy or precision of the data values within the Result.'),
    'relationshiptype': _get_vocabulary(cvmodels.RelationshipType, 'A vocabulary for describing the type of relationship between two entities in an ODM2 database. Examples include related Actions, Results, datasets, etc. The RelationshipType describes the nature of the relationship between the two entity instances (e.g., a Specimen SamplingFeature "was collected at" a Site SamplingFeature).'),
    'medium': _get_vocabulary(cvmodels.Medium, 'A vocabulary for describing the physical medium of a specimen, reference material, or sampled environment.'),
    'unitstype': _get_vocabulary(cvmodels.UnitsType, 'A vocabulary for describing the type of the Unit or the more general quantity that the Unit represents.'),
}

requests = {
    # optional keys:
    # list_view, create_view, update_view, list_template, create_template, update_template

    'actiontyperequest': _get_request(cvmodels.ActionTypeRequest, 'actiontype', cvmodels.ActionType),
    'methodtyperequest': _get_request(cvmodels.MethodTypeRequest, 'methodtype', cvmodels.MethodType),
    'aggregationstatisticrequest': _get_request(cvmodels.AggregationStatisticRequest, 'aggregationstatistic', cvmodels.AggregationStatistic),
    'annotationtyperequest': _get_request(cvmodels.AnnotationTypeRequest, 'annotationtype', cvmodels.AnnotationType),
    'censorcoderequest': _get_request(cvmodels.CensorCodeRequest, 'censorcode', cvmodels.CensorCode),
    'datasettyperequest': _get_request(cvmodels.DatasetTypeRequest, 'datasettype', cvmodels.DatasetType),
    'directivetyperequest': _get_request(cvmodels.DirectiveTypeRequest, 'directivetype', cvmodels.DirectiveType),
    'elevationdatumrequest': _get_request(cvmodels.ElevationDatumRequest, 'elevationdatum', cvmodels.ElevationDatum),
    'equipmenttyperequest': _get_request(cvmodels.EquipmentTypeRequest, 'equipmenttype', cvmodels.EquipmentType),
    'organizationtyperequest': _get_request(cvmodels.OrganizationTypeRequest, 'organizationtype', cvmodels.OrganizationType),
    'propertydatatyperequest': _get_request(cvmodels.PropertyDataTypeRequest, 'propertydatatype', cvmodels.PropertyDataType),
    'qualitycoderequest': _get_request(cvmodels.QualityCodeRequest, 'qualitycode', cvmodels.QualityCode),
    'resulttyperequest': _get_request(cvmodels.ResultTypeRequest, 'resulttype', cvmodels.ResultType),
    'samplingfeaturegeotyperequest': _get_request(cvmodels.SamplingFeatureGeotypeRequest, 'samplingfeaturegeotype', cvmodels.SamplingFeatureGeotype),
    'samplingfeaturetyperequest': _get_request(cvmodels.SamplingFeatureTypeRequest, 'samplingfeaturetype', cvmodels.SamplingFeatureType),
    'sitetyperequest': _get_request(cvmodels.SiteTypeRequest, 'sitetype', cvmodels.SiteType),
    'spatialoffsettyperequest': _get_request(cvmodels.SpatialOffsetTypeRequest, 'spatialoffsettype', cvmodels.SpatialOffsetType),
    'speciationrequest': _get_request(cvmodels.SpeciationRequest, 'speciation', cvmodels.Speciation),
    'specimentyperequest': _get_request(cvmodels.SpecimenTypeRequest, 'specimentype', cvmodels.SpecimenType),
    'statusrequest': _get_request(cvmodels.StatusRequest, 'status', cvmodels.Status),
    'taxonomicclassifiertyperequest': _get_request(cvmodels.TaxonomicClassifierTypeRequest, 'taxonomicclassifiertype', cvmodels.TaxonomicClassifierType),
    'variablenamerequest': _get_request(cvmodels.VariableNameRequest, 'variablename', cvmodels.VariableName),
    'variabletyperequest': _get_request(cvmodels.VariableTypeRequest, 'variabletype', cvmodels.VariableType),
    'dataqualitytyperequest': _get_request(cvmodels.DataQualityTypeRequest, 'dataqualitytype', cvmodels.DataQualityType),
    'relationshiptyperequest': _get_request(cvmodels.RelationshipTypeRequest, 'relationshiptype', cvmodels.RelationshipType),
    'mediumrequest': _get_request(cvmodels.MediumRequest, 'medium', cvmodels.Medium),
    'unitstyperequest': _get_request(cvmodels.UnitsTypeRequest, 'unitstype', cvmodels.UnitsType),
}
