import re
from typing import List, Type, Tuple, Dict, Any

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from django.db import models

from cvservices.cv_fields_abstractions import AbstractUnitsType, AbstractActionType, AbstractSpatialOffsetType
from odm2cvs.controlled_vocabularies import vocabularies

vocabulary_models = {}
requests_models = {}


class ControlledVocabularyAbstraction(models.Model):
    term = models.CharField(max_length=255, help_text="Please enter a URI-friendly version of your term with no spaces, special characters, etc.")
    name = models.CharField(max_length=255, help_text="Please enter the term as you would expect it to appear in a sentence.")
    definition = models.TextField(help_text="Please enter a detailed definition of the term.", blank=True, default='')
    category = models.CharField(max_length=255, blank=True, default='', help_text="You may suggest a category for the term. Refer to the vocabulary to see which categories have been used. You may also suggest a new category.")
    provenance = models.TextField(blank=True, default='', help_text="Enter a note about where the term came from. If you retrieved the definition of the term from a website or other source, note that here.")
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True, default='', max_length=1024, help_text="If you retrieved the term from another formal vocabulary system, enter the URI of the term from the other system here.")
    note = models.TextField(blank=True, default='', help_text="Please enter any additional notes you may have about the term.")

    class Meta:
        abstract = True


class ControlledVocabulary(ControlledVocabularyAbstraction):
    CURRENT = 'Current'
    ARCHIVED = 'Archived'

    STATUS_CHOICES = [
        (CURRENT, 'Current'),
        (ARCHIVED, 'Archived')
    ]

    vocabulary_id = models.AutoField(primary_key=True)
    vocabulary_status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=CURRENT)
    previous_version = models.OneToOneField('self', blank=True, null=True, related_name='revised_version', on_delete=models.CASCADE)

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


class ControlledVocabularyRequest(ControlledVocabularyAbstraction):
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
    status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=PENDING)
    date_submitted = models.DateField(db_column='dateSubmitted', default=timezone.now)
    date_status_changed = models.DateField(db_column='dateStatusChanged', default=timezone.now)
    request_notes = models.TextField(db_column='requestNotes', blank=True, default='')
    submitter_name = models.CharField(max_length=255, db_column='submitterName', help_text="Enter your name.")
    submitter_email = models.CharField(max_length=255, db_column='submitterEmail', help_text="Enter your email address.")
    request_reason = models.TextField(db_column='requestReason', help_text="Please enter a brief description of the reason for your submission (e.g., Term does not exist yet, Term is needed for my data use case, etc.)")

    request_for = models.ForeignKey('ControlledVocabulary', db_column='requestFor', blank=True, null=True, on_delete=models.CASCADE)
    original_request = models.ForeignKey('self', db_column='originalRequestId', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'requests'
        ordering = ["date_submitted", "-request_id"]


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    term = models.CharField(max_length=255, db_column='Term')
    type = models.CharField(max_length=255, db_column='UnitsTypeCV')
    abbreviation = models.CharField(max_length=255, blank=True, default='', db_column='UnitsAbbreviation')
    name = models.CharField(max_length=255, db_column='UnitsName')
    link = models.URLField(max_length=1024, blank=True, default='', db_column='UnitsLink')

    class Meta:
        db_table = 'units'
        ordering = ["type"]


def generate_specific_models() -> None:
    """
    Generates all vocabulary and requests models from the vocabularies defines in odm2cvs.controlled_vocabularies.
    :return:
    """
    def create_meta_class(name: str, table_name: str, ordering_fields: List[str]) -> Type:
        """

        :param name: Verbose vocabulary name.
        :param table_name: Database table name.
        :param ordering_fields: List of fields to order the vocabulary by.
        :return:
        """
        class Meta:
            verbose_name = name
            db_table = table_name
            ordering = ordering_fields

        return Meta

    vocabulary_parent: Tuple[Type] = (ControlledVocabulary, )
    request_parent: Tuple[Type] = (ControlledVocabularyRequest, )

    vocabulary_name: str
    vocabulary: Dict[str, Any]
    for vocabulary_name, vocabulary in vocabularies.items():
        # vocabulary metadata
        verbose_name: str = vocabulary.get('name')
        classname: str = vocabulary.get('classname', re.sub('[^A-Za-z0-9]+', '', verbose_name))
        table_name: str = vocabulary.get('table_name', f'{vocabulary_name}cv')
        abstract_parents: Tuple[Type] = vocabulary.get('abstract_parents', ())
        vocabulary_ordering: List[str] = vocabulary.get('ordering', ControlledVocabulary._meta.ordering)

        # request metadata
        request_name: str = f'{verbose_name} Request'
        request_classname: str = f'{classname}Request'
        request_ordering: List[str] = ControlledVocabularyRequest._meta.ordering

        # create vocabulary and request models
        vocabulary_model: Type = type(classname, vocabulary_parent + abstract_parents, {
            '__module__': 'cvservices.models',
            'Meta': create_meta_class(verbose_name, table_name, vocabulary_ordering)
        })

        request_model: Type = type(request_classname, request_parent + abstract_parents, {
            '__module__': 'cvservices.models',
            'Meta': create_meta_class(request_name, f'{table_name}requests', request_ordering)
        })

        # update vocabulary dictionary with generated models and request
        vocabulary['model'] = vocabulary_model
        vocabulary['request'] = vocabulary.get('request', {})
        vocabulary['request']['model'] = request_model
        vocabulary['request']['name'] = request_name

        vocabulary_models[vocabulary_name] = vocabulary_model
        requests_models[vocabulary_name] = request_model

        # Add models to module scope
        globals()[classname] = vocabulary_model
        globals()[request_classname] = request_model


generate_specific_models()
