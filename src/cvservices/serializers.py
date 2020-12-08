from typing import Union, Dict, Any

from django.db.models import QuerySet
from rest_framework import serializers

from cvservices.models import ControlledVocabulary
from odm2cvs.controlled_vocabularies import rdf_field_relations


class VocabularySerializer(serializers.BaseSerializer):
    """
    A read-only Vocabulary serializer that presents all the fields
    specified in `controlled_vocabularies.rdf_field_relations` in a primitive dictionary.
    """

    def to_representation(self, vocabulary_instance: Union[ControlledVocabulary, QuerySet]) -> Dict[str, Any]:
        vocabulary_data: Dict[str, Any] = {}
        for attribute_name in rdf_field_relations.keys():
            if not hasattr(vocabulary_instance, attribute_name):
                continue
            vocabulary_data[attribute_name] = vocabulary_instance.__getattribute__(attribute_name)
        return vocabulary_data

    def to_internal_value(self, data):
        pass

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
