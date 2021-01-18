from django.core.management.base import BaseCommand

from odm2cvs.controlled_vocabularies import vocabularies


class Command(BaseCommand):
    help = 'Deletes every object in the database'

    def handle(self, *args, **options):
        for vocabulary_code, vocabulary in vocabularies.items():
            vocabulary.get('model').objects.all().delete()
            vocabulary.get('request').get('model').objects.all().delete()
