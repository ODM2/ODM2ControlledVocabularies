import csv
from io import StringIO
from typing import Union, Dict, List, KeysView

from django.http import HttpRequest
from django.urls import reverse
from rdflib import Graph, SKOS, RDF, DC, URIRef, Literal, Namespace
from rest_framework import renderers

from odm2cvs.controlled_vocabularies import rdf_namespace, Vocabulary, rdf_field_relations


class RDFRenderer(renderers.BaseRenderer):
    excluded_fields = ['term']
    media_type = 'text/plain'
    # media_type = 'application/rdf+xml'
    format = 'skos'

    def render(self, data: Union[Dict, List[Dict]], media_type: str = None, renderer_context=None) -> str:
        """
        Receives an already serialized object/list of objects and converts it to a SKOS file.
        :param data: An individual or a list of serialized controlled vocabulary objects.
        :param media_type: The media type of the request.
        :param renderer_context: The renderer context.
        :return: A SKOS RDF rendition of the serialized controlled vocabulary.
        """
        if data is None:
            return ''

        if not isinstance(data, list):
            data = [data]

        request: HttpRequest = renderer_context['request']
        vocabulary: Vocabulary = renderer_context['view'].vocabulary

        # create graph
        graph: Graph = Graph()

        # define and bind custom namespace
        namespace: Namespace = Namespace(rdf_namespace.get('uri'))
        graph.bind(rdf_namespace.get('name'), namespace)
        graph.bind('skos', SKOS)
        graph.bind('dc', DC)

        namespace_map: Dict[str, Namespace] = {
            rdf_namespace.get('name'): namespace,
            'skos': SKOS
        }

        # add a skos ConceptScheme class with the vocabulary metadata
        scheme_uri: str = request.build_absolute_uri(reverse(vocabulary.get('list_url_name')))
        title: str = f'{vocabulary.get("name")} Controlled Vocabulary'
        scheme_creator: str = rdf_namespace.get('creator')

        graph.add((URIRef(scheme_uri), RDF['type'], SKOS['ConceptScheme']))
        graph.add((URIRef(scheme_uri), DC['title'], Literal(title)))
        graph.add((URIRef(scheme_uri), DC['creator'], Literal(scheme_creator)))
        graph.add((URIRef(scheme_uri), DC['description'], Literal(vocabulary.get('description'))))

        # add a skos concept class for each vocabulary term
        for concept in data:
            relative_uri: str = reverse(vocabulary.get('detail_url_name'), args=[concept.get('term')])
            concept_uri: str = request.build_absolute_uri(relative_uri)
            graph.add((URIRef(concept_uri), RDF['type'], SKOS['Concept']))
            graph.add((URIRef(concept_uri), SKOS['inScheme'], URIRef(scheme_uri)))

            # add each field from `rdf_field_relations`
            for fieldname, field in rdf_field_relations.items():
                if fieldname not in concept or concept.get(fieldname) == '' or fieldname in self.excluded_fields:
                    continue
                field_namespace: Namespace = namespace_map[field.get('namespace')]
                graph.add((URIRef(concept_uri), field_namespace[field.get('node')], Literal(concept.get(fieldname))))

        return graph.serialize(format='xml')


class CSVRenderer(renderers.BaseRenderer):
    media_type: str = 'text/csv'
    format: str = 'csv'

    def render(self, data: Union[Dict, List[Dict]], media_type: str = None, renderer_context=None) -> str:
        """
        Receives an already serialized object/list of objects and converts it to a csv file.
        :param data: An individual or a list of serialized controlled vocabulary objects.
        :param media_type: The media type of the request.
        :param renderer_context: The renderer context.
        :return: A CSV rendition of the serialized controlled vocabulary.
        """
        if data is None:
            return ''

        if not isinstance(data, list):
            data = [data]

        # Create string buffer to store hold the csv file content
        csv_buffer: StringIO = StringIO()
        # Get the fieldnames from the first object in the data
        fieldnames: KeysView = data[0].keys()
        # Create a CSV writer with the string buffer
        csv_writer: csv.DictWriter = csv.DictWriter(csv_buffer, fieldnames=fieldnames)
        # Write the headers and data to the CSV writer
        csv_writer.writeheader()
        csv_writer.writerows(data)
        # Return the contents of the writer
        return csv_buffer.getvalue()
