"""
This is the module that defines all the vocabularies
and it is the source of all the vocabulary and vocabulary request models.

The format for each vocabulary is the following:

'{vocabulary short name}': {
    'name': {string: verbose name},
    'classname':(optional) {string: the name of the model class. defaults to the verbose name without spaces},
    'description': {string: a description of the vocabulary},
    'db_table':(optional) {string: the name of the database table for this vocabulary model. short name is used if not present.},
    'abstract_parents':(optional) {tuple: A tuple with all the abstract model classes containing any extra fields},
    'ordering':(optional) {list: a list with the name(s) of field(s) that will be used for the default ordering},
    'list_view':(optional) {ListView: a custom list view},
    'detail_view':(optional) {DetailView: a custom detail view},
    'list_template':(optional) {string: a custom list template},
    'detail_template':(optional) {string: a custom detail template},
    'request': {
        'list_view':(optional) {ListView: a custom request list view},
        'create_view':(optional) {CreateView: a custom request create view},
        'update_view':(optional) {UpdateView: a custom request update view},
        'list_template':(optional) {string: a custom request list template},
        'create_template':(optional) {string: a custom request create template},
        'update_template':(optional) {string: a custom request update template},
    }
}


The links between the Controlled Vocabularies fields and SKOS are defined in
the `rdf_field_relations` and `rdf_namespace_references` dictionaries.


The format for each field relation is the following:

'{controlled vocabulary field name}': {
    'node': '{string: rdf equivalent tag}',
    'namespace': '{string: namespace to be used for the rdf tag}'
},


For the custom rdf namespace, the format is the following:

{
    'name': '{string: namespace name}',
    'uri': '{string: URL reference to the namespace}',
    'creator': '{string: The Controlled Vocabularies creator}'
}

"""

from typing import Dict, Any, Type

from django.dispatch import receiver

from cvservices.signals import model_created
from odm2cvs.cv_specific_fields import AbstractActionType, AbstractSpatialOffsetType, AbstractUnitsType

Vocabulary = Dict[str, Any]
VocabularyRequest = Dict[str, Any]


@receiver(model_created)
def update_vocabularies_dict(sender: Type, **kwargs) -> None:
    vocabulary_code: str = kwargs.get('vocabulary_code')
    vocabulary_model: Type = kwargs.get('vocabulary_model', sender)
    request_model: Type = kwargs.get('request_model')

    vocabulary: Vocabulary = vocabularies.get(vocabulary_code)
    vocabulary['model'] = vocabulary_model
    vocabulary['list_url_name'] = f'{vocabulary_code}'
    vocabulary['detail_url_name'] = f'{vocabulary_code}_detail'
    vocabulary['api_list_url_name'] = f'{vocabulary_code}_api_list'
    vocabulary['api_detail_url_name'] = f'{vocabulary_code}_api_detail'

    request: VocabularyRequest = vocabulary.get('request', {})
    request['model'] = request_model
    request['name'] = f'{vocabulary["name"]} Request'
    request['list_url_name'] = f'{vocabulary_code}request'
    request['create_url_name'] = f'{vocabulary_code}request_form'
    request['update_url_name'] = f'{vocabulary_code}request_update_form'
    vocabulary['request'] = request


vocabularies: Dict[str, Vocabulary] = {
    'actiontype': {
        'name': 'Action Type',
        'description': 'A vocabulary for describing the type of actions performed in making observations. Depending on the action type, the action may or may not produce an observation result.',
        'abstract_parents': (AbstractActionType, ),
    },
    'methodtype': {
        'name': 'Method Type',
        'description': 'A vocabulary for describing types of Methods associated with creating observations. MethodTypes correspond with ActionTypes in ODM2. An Action must be performed using an appropriate MethodType - e.g., a specimen collection Action should be associated with a specimen collection method.',
    },
    'aggregationstatistic': {
        'name': 'Aggregation Statistic',
        'description': 'A vocabulary for describing the calculated statistic associated with recorded observations. The aggregation statistic is calculated over the time aggregation interval associated with the recorded observation. ',
    },
    'annotationtype': {
        'name': 'Annotation Type',
        'description': 'A vocabulary for describing the type of annotation. In ODM2 the annotation type determines whether the annotation forms a grouping of related entities (e.g., a group of sites or variables) or an annotation of a particular entity (e.g., a comment about an individual Site or data value). ',
    },
    'censorcode': {
        'name': 'Censor Code',
        'description': 'A vocabulary for describing whether a data value was determined or whether the actual value is unknown due to right or left censoring.',
    },
    'datasettype': {
        'name': 'Dataset Type',
        'description': 'A vocabulary for describing types of Datasets in ODM2. Datasets are logical groupings of Results.',
    },
    'directivetype': {
        'name': 'Directive Type',
        'description': 'A vocabulary for describing types of directives under which observations are made. Examples include projects, monitoring programs, campaigns, etc.',
    },
    'elevationdatum': {
        'name': 'Elevation Datum',
        'description': 'A vocabulary for describing vertical datums. Vertical datums are used in ODM2 to specify the origin for elevations assocated with SamplingFeatures.',
    },
    'equipmenttype': {
        'name': 'Equipment Type',
        'description': 'A vocabulary for describing types of equipment used for making observations. Examples include sensors, batteries, radios, dataloggers, samplers, etc.',
    },
    'organizationtype': {
        'name': 'Organization Type',
        'description': 'A vocabulary for describing types of Organizations. In ODM2, People may or may not be affiliated with an Organization. People can also be affiliated with more than one Organization.',
    },
    'propertydatatype': {
        'name': 'Property Data Type',
        'description': 'A vocabulary for describing the data type for an extension property in ODM2.  Extension properties can be added to many of the entities in ODM2 (e.g., Sites, Variables, etc.). The values of these extension properties must be of one of the listed primitive data types.',
    },
    'qualitycode': {
        'name': 'Quality Code',
        'description': 'A vocabulary for describing the quality of the observation.',
    },
    'resulttype': {
        'name': 'Result Type',
        'description': 'A vocabulary for describing the type of the Result. In ODM2 Results are separated from, but related to their data values. Each ResultType has a set of related tables for storing the data values for any result of that type.',
    },
    'samplingfeaturegeotype': {
        'name': 'Sampling Feature Geo-type',
        'description': 'A vocabulary for describing the geospatial feature type associated with a SamplingFeature. For example, Site SamplingFeatures are represented as points. In ODM2, each SamplingFeature may have only one geospatial type, but a geospatial types may range from simple points to a complex polygons or even three dimensional volumes.',
    },
    'samplingfeaturetype': {
        'name': 'Sampling Feature Type',
        'description': 'A vocabulary for describing the type of SamplingFeature. Many different SamplingFeature types can be represented in ODM2. SamplingFeatures of type Site and Specimen will be the most common, but many different types of varying levels of complexity can be used.',
    },
    'sitetype': {
        'name': 'Site Type',
        'description': 'A vocabulary for describing the type of a data collection Site. To some extent, these types represent the ultimate feature of interest that the site was established to measure. For example, a Stream Site was established to measure properties of a Stream.',
    },
    'spatialoffsettype': {
        'name': 'Spatial Offset Type',
        'description': 'A vocabulary for describing the type of SpatialOffset that exists between two SamplingFeatures.',
        'abstract_parents': (AbstractSpatialOffsetType,),
    },
    'speciation': {
        'name': 'Speciation',
        'description': 'A vocabulary for describing the speciation in which a measured variable is expressed.',
    },
    'specimentype': {
        'name': 'Specimen Type',
        'description': 'A vocabulary for describing the type of a physical Specimen.',
    },
    'status': {
        'name': 'Status',
        'description': 'A vocabulary for describing the data collection status of a Result. In ODM2 the StatusCV can be used to specify whether data collection is planned, ongoing, or complete.',
    },
    'taxonomicclassifiertype': {
        'name': 'Taxonomic Classifier Type',
        'description': 'A vocabulary for describing types of taxonomies from which descriptive terms used in an ODM2 database have been drawn. Taxonomic classifiers provide a way to classify Results and Specimens according to terms from a formal taxonomy.',
    },
    'variablename': {
        'name': 'Variable Name',
        'description': 'A vocabulary for describing the name of Variables.',
    },
    'variabletype': {
        'name': 'Variable Type',
        'description': 'A vocabulary for describing the type of Variables. VariableTypes provide a way to group Variables into categories for easier querying and filtering.',
    },
    'dataqualitytype': {
        'name': 'Data Quality Type',
        'description': 'A vocabulary for describing the type of data quality information provided for a particular Result. Examples include the accuracy or precision of the data values within the Result.',
    },
    'relationshiptype': {
        'name': 'Relationship Type',
        'description': 'A vocabulary for describing the type of relationship between two entities in an ODM2 database. Examples include related Actions, Results, datasets, etc. The RelationshipType describes the nature of the relationship between the two entity instances (e.g., a Specimen SamplingFeature "was collected at" a Site SamplingFeature).',
    },
    'medium': {
        'name': 'Medium',
        'description': 'A vocabulary for describing the physical medium of a specimen, reference material, or sampled environment.',
    },
    'unitstype': {
        'name': 'Units Type',
        'description': 'A vocabulary for describing the type of the Unit or the more general quantity that the Unit represents.',
        'abstract_parents': (AbstractUnitsType,),
    },
}


rdf_namespace: Dict[str, str] = {
    'name': 'odm2',
    'uri': 'http://vocabulary.odm2.org/',
    'creator': 'ODM2 Working Group'
}


rdf_field_relations: Dict[str, Dict[str, str]] = {
    'term': {
        'node': 'Concept',
        'namespace': 'skos'
    },
    'name': {
        'node': 'prefLabel',
        'namespace': 'skos'
    },
    'definition': {
        'node': 'definition',
        'namespace': 'skos'
    },
    'category': {
        'node': 'category',
        'namespace': 'odm2'
    },
    'provenance': {
        'node': 'historyNote',
        'namespace': 'skos'
    },
    'provenance_uri': {
        'node': 'exactMatch',
        'namespace': 'skos'
    },
    'note': {
        'node': 'note',
        'namespace': 'skos'
    },
    'produces_result': {
        'node': 'producesResult',
        'namespace': 'odm2'
    },
    'offset1': {
        'node': 'offset1',
        'namespace': 'odm2'
    },
    'offset2': {
        'node': 'offset2',
        'namespace': 'odm2'
    },
    'offset3': {
        'node': 'offset3',
        'namespace': 'odm2'
    },
    'default_unit': {
        'node': 'defaultUnit',
        'namespace': 'odm2'
    },
    'dimension_symbol': {
        'node': 'dimensionSymbol',
        'namespace': 'odm2'
    },
    'dimension_length': {
        'node': 'dimensionLength',
        'namespace': 'odm2'
    },
    'dimension_mass': {
        'node': 'dimensionMass',
        'namespace': 'odm2'
    },
    'dimension_time': {
        'node': 'dimensionTime',
        'namespace': 'odm2'
    },
    'dimension_current': {
        'node': 'dimensionCurrent',
        'namespace': 'odm2'
    },
    'dimension_temperature': {
        'node': 'dimensionTemperature',
        'namespace': 'odm2'
    },
    'dimension_amount': {
        'node': 'dimensionAmount',
        'namespace': 'odm2'
    },
    'dimension_light': {
        'node': 'dimensionLight',
        'namespace': 'odm2'
    }
}
