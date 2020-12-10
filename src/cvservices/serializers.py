from collections import OrderedDict
from typing import Union, Dict, Any, List
from typing import OrderedDict as OrderedDictionary

from django.core.exceptions import FieldDoesNotExist
from django.db.models import QuerySet, Field
from rest_framework import serializers

from cvservices.models import ControlledVocabulary, Unit
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


class UnitsSerializer(serializers.BaseSerializer):
    """
        A read-only Units serializer that represents the data as an ordered dictionary,
        and uses the field's column names instead of the field names as keys.
    """
    fields: List[str] = ['term', 'name', 'type', 'abbreviation', 'link']

    def get_model_fields(self) -> OrderedDictionary[str, Field]:
        fields: OrderedDictionary[str, Field] = OrderedDict()
        for field_name in self.fields:
            try:
                field: Field = Unit._meta.get_field(field_name)
            except FieldDoesNotExist:
                continue
            fields[field.name] = field
        return fields

    def to_representation(self, instance: Unit) -> OrderedDictionary[str, str]:
        serialized_dict: OrderedDictionary[str, str] = OrderedDict()
        fields: OrderedDictionary[str, Field] = self.get_model_fields()

        for field_name, field in fields.items():
            value: str = field.value_from_object(instance)
            serialized_dict[field.db_column] = value

        return serialized_dict

    def to_internal_value(self, data):
        pass

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
