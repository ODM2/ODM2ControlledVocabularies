import csv
from django.core.management import BaseCommand

from cvinterface.controlled_vocabularies import vocabularies


class Command(BaseCommand):
    help = 'Sets the download links for raw and controlled data.'

    def add_arguments(self, parser):
        parser.add_argument('vocabulary', type=str, help='The destination vocabulary.')
        parser.add_argument('file', type=str, help='CSV formatted list of new terms.')

    def handle(self, *args, **options):
        csv_file = options['file']
        vocabulary_name = options['vocabulary']
        Vocabulary = vocabularies[vocabulary_name]['model']

        with open(csv_file) as f:
            reader = csv.DictReader(f)
            term_counter = 0
            
            for row in reader:
                vocabulary, was_created = Vocabulary.objects.get_or_create(
                    term=row['term'],
                    name=row['name'],
                    definition=row['definition'],
                    category='',
                    provenance=row['provenance'],
                    provenance_uri=row['provenanceURI'],
                    note=row['note']
                )
                if not was_created:
                    print('-- term {} was already in the database.'.format(vocabulary.term))
                    continue
                print('- term {} added.'.format(vocabulary.term))
                term_counter += 1

        print('{} new terms added to the {} vocabulary'.format(term_counter, vocabularies[vocabulary_name]['name']))
