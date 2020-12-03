from rest_framework import serializers, renderers

from cvservices.models import ControlledVocabulary
from odm2cvs.controlled_vocabularies import rdf_field_relations


class VocabularySerializer(serializers.BaseSerializer):
    """
    A read-only Vocabulary serializer that presents all the fields
    specified in `controlled_vocabularies.rdf_field_relations` in a primitive dictionary.
    """

    def to_representation(self, vocabulary_instance: ControlledVocabulary):
        vocabulary_data = {}
        for attribute_name in rdf_field_relations.keys():
            if not hasattr(vocabulary_instance, attribute_name):
                continue
            vocabulary_data[attribute_name] = vocabulary_instance.__getattribute__(attribute_name)

    def to_internal_value(self, data):
        pass

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class RDFRenderer(renderers.BaseRenderer):
    media_type = 'application/rdf+xml'
    format = 'skos'

    def render(self, data, media_type=None, renderer_context=None):
        return {}


class CSVRenderer(renderers.BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'

    def render(self, data, media_type=None, renderer_context=None):
        return {}
