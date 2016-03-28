from django.conf.urls import url
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from tastypie.bundle import Bundle
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils.mime import build_content_type
from cvservices.models import ControlledVocabulary

from .models import Scheme, FieldRelation

from rdflib import Graph, URIRef, Literal
from rdflib import Namespace
from rdflib.namespace import SKOS, RDF

from collections import OrderedDict
import csv
import StringIO


class RdfSerializer(Serializer):
    formats = ['json', 'skos', 'csv']
    content_types = {
        'json': 'application/json',
        'skos': 'text/plain',
        'csv': 'text/csv'
    }

    def to_csv(self, data, options=None):
        first = True
        options = options or {}
        excluded_fields = [u'vocabulary_id', u'vocabulary_status', u'resource_uri']
        raw_data = StringIO.StringIO()
        data = self.to_simple(data, options)

        # Entire CV
        if "meta" in data.keys():
            objects = data.get("objects")

            for value in objects:
                test = {}
                for excluded_field in excluded_fields:
                    del value[excluded_field]
                self.flatten(value, test)

                odict = OrderedDict()
                odict['term'] = test['term']
                del test['term']
                odict['name'] = test['name']
                del test['name']
                odict['definition'] = test['definition']
                del test['definition']
                odict['category'] = test['category']
                del test['category']
                odict['provenance'] = test['provenance']
                del test['provenance']
                odict['provenance_uri'] = test['provenance_uri']
                del test['provenance_uri']
                odict['note'] = test['note']
                del test['note']
                if 'default_unit' in test:
                    odict['default_unit'] = test['default_unit']
                    del test['default_unit']
                if 'dimension_symbol' in test:
                    odict['dimension_symbol'] = test['dimension_symbol']
                    del test['dimension_symbol']
                if 'dimension_length' in test:
                    odict['dimension_length'] = test['dimension_length']
                    del test['dimension_length']
                if 'dimension_mass' in test:
                    odict['dimension_mass'] = test['dimension_mass']
                    del test['dimension_mass']
                if 'dimension_time' in test:
                    odict['dimension_time'] = test['dimension_time']
                    del test['dimension_time']
                if 'dimension_current' in test:
                    odict['dimension_current'] = test['dimension_current']
                    del test['dimension_current']
                if 'dimension_temperature' in test:
                    odict['dimension_temperature'] = test['dimension_temperature']
                    del test['dimension_temperature']
                if 'dimension_amount' in test:
                    odict['dimension_amount'] = test['dimension_amount']
                    del test['dimension_amount']
                if 'dimension_light' in test:
                    odict['dimension_light'] = test['dimension_light']
                    del test['dimension_light']

                odict.update(test)
                writer = csv.DictWriter(raw_data, odict.keys())

                if first:
                    writer = csv.DictWriter(raw_data, odict.keys())
                    writer.writeheader()
                    writer.writerow(odict)
                    first = False
                else:
                    writer.writerow({k: (v.encode('utf-8') if isinstance(v, int) is not True and isinstance(v, type(
                        None)) is not True else v) for k, v in odict.items()})

        # Single Term
        else:
            test = {}
            for excluded_field in excluded_fields:
                del data[excluded_field]

            self.flatten(data, test)
            odict = OrderedDict()
            odict['term'] = test['term']
            del test['term']
            odict['name'] = test['name']
            del test['name']
            odict['definition'] = test['definition']
            del test['definition']
            odict['category'] = test['category']
            del test['category']
            odict['provenance'] = test['provenance']
            del test['provenance']
            odict['provenance_uri'] = test['provenance_uri']
            del test['provenance_uri']
            odict['note'] = test['note']
            del test['note']

            if 'default_unit' in test:
                odict['default_unit'] = test['default_unit']
                del test['default_unit']
            if 'dimension_symbol' in test:
                odict['dimension_symbol'] = test['dimension_symbol']
                del test['dimension_symbol']
            if 'dimension_length' in test:
                odict['dimension_length'] = test['dimension_length']
                del test['dimension_length']
            if 'dimension_mass' in test:
                odict['dimension_mass'] = test['dimension_mass']
                del test['dimension_mass']
            if 'dimension_time' in test:
                odict['dimension_time'] = test['dimension_time']
                del test['dimension_time']
            if 'dimension_current' in test:
                odict['dimension_current'] = test['dimension_current']
                del test['dimension_current']
            if 'dimension_temperature' in test:
                odict['dimension_temperature'] = test['dimension_temperature']
                del test['dimension_temperature']
            if 'dimension_amount' in test:
                odict['dimension_amount'] = test['dimension_amount']
                del test['dimension_amount']
            if 'dimension_light' in test:
                odict['dimension_light'] = test['dimension_light']
                del test['dimension_light']

            odict.update(test)

            writer = csv.DictWriter(raw_data, odict.keys())
            if first:
                writer.writeheader()
                writer.writerow({k: (
                    v.encode('utf-8') if isinstance(v, int) is not True and isinstance(v, type(
                        None)) is not True else v) for k, v in odict.items()})
                first = False
            else:
                writer.writerow(odict)

        csv_content = raw_data.getvalue()
        return csv_content

    def flatten(self, data, odict={}):
        if isinstance(data, list):
            for value in data:
                self.flatten(value, odict)
        elif isinstance(data, dict):
            for (key, value) in data.items():
                if not isinstance(value, (dict, list)):
                    odict[key] = value
                else:
                    self.flatten(value, odict)

    def to_skos(self, data, options=None):
        """
        Given some data, converts that data to an rdf skos format in xml.
        """
        # element = {}
        # get scheme: resource being requested. actionTypeCV, methodTypeCV, etc.

        scheme = Scheme.objects.get(name=options['scheme'])
        excluded_fields = [u'term', u'resource_uri', u'vocabulary_id', u'vocabulary_status']

        baseURI = 'http://vocabulary.odm2.org/ODM2/ODM2Terms/'
        graph = Graph()
        odm2 = Namespace(baseURI)
        dc = Namespace('http://purl.org/dc/elements/1.1/')

        graph.bind('odm2', odm2)
        graph.bind('skos', SKOS)
        graph.bind('dc', dc)

        # If requesting an entire CV.
        if isinstance(data, dict):
            # print data
            # Add a SKOS ConceptScheme class to the graph.
            (graph.add((URIRef(scheme.uri), RDF['type'],
                        SKOS['ConceptScheme'])))
            (graph.add((URIRef(scheme.uri), dc['title'],
                        Literal(scheme.title))))
            (graph.add((URIRef(scheme.uri), dc['creator'],
                        Literal(scheme.creator))))
            (graph.add((URIRef(scheme.uri), dc['description'],
                        Literal(scheme.description))))

            # For each concept in the requested CV, create a SKOS Concept class.
            for concept in data[u'objects']:
                (graph.add((URIRef(scheme.uri + '/' + concept.obj.term),
                            RDF['type'], SKOS['Concept'])))
                (graph.add((URIRef(scheme.uri + '/' + concept.obj.term),
                            SKOS['inScheme'], URIRef(scheme.uri))))

                # Add labels to each concept class.
                for x in concept.data:
                    label = concept.data[x]
                    if isinstance(label, type(None)):
                        label = ''
                    if isinstance(label, int):
                        label = str(label)
                    # Skip excluded field elements.
                    if x in excluded_fields:
                        continue
                    # Skip empty elements.
                    elif label.rstrip('\r\n') == '':
                        continue
                    else:
                        alias = str(FieldRelation.objects.get(
                            field_name=x).node.namespace)
                        if alias == 'odm2':
                            (graph.add((URIRef(scheme.uri + '/' +
                                               concept.obj.term),
                                        odm2[FieldRelation.objects
                                        .get(field_name=x).node.name],
                                        Literal(
                                            label.rstrip('\r\n')))))
                        else:
                            (graph.add((URIRef(scheme.uri + '/' +
                                               concept.obj.term),
                                        SKOS[FieldRelation.objects
                                        .get(field_name=x).node.name],
                                        Literal(label.rstrip('\r\n')))))

        # If requesting a single Concept
        elif isinstance(data, Bundle):
            # Add a SKOS ConceptScheme class to the graph.
            (graph.add((URIRef(scheme.uri), RDF['type'],
                        SKOS['ConceptScheme'])))
            (graph.add((URIRef(scheme.uri), dc['title'],
                        Literal(scheme.title))))
            (graph.add((URIRef(scheme.uri), dc['creator'],
                        Literal(scheme.creator))))
            (graph.add((URIRef(scheme.uri), dc['description'],
                        Literal(scheme.description))))

            # Add a SKOS Concept class to the graph.
            (graph.add((URIRef(scheme.uri + '/' + data.obj.term),
                        RDF['type'], SKOS['Concept'])))
            (graph.add((URIRef(scheme.uri + '/' + data.obj.term),
                        SKOS['inScheme'], URIRef(scheme.uri))))

            # Add labels within concept class.
            for field in data.data.keys():
                label = data.data[field]
                if isinstance(label, type(None)):
                    label = ''
                if isinstance(label, int):
                    label = str(label)

                if field in excluded_fields:
                    continue
                elif label.rstrip('\r\n') == '':
                    continue
                else:
                    relation = FieldRelation.objects.get(field_name=field)
                    alias = relation.node.namespace.alias
                    if alias == u'odm2':
                        (graph.add((URIRef(scheme.uri + '/' + data.obj.term),
                                    odm2[FieldRelation.objects
                                    .get(field_name=field).node.name],
                                    Literal(label.rstrip('\r\n')))))
                    else:
                        (graph.add((URIRef(scheme.uri + '/' + data.obj.term),
                                    SKOS[FieldRelation.objects
                                    .get(field_name=field).node.name],
                                    Literal(label.rstrip('\r\n')))))
        else:
            pass
        # Returning the graph serialized into 'xml' format rather than
        # 'pretty-xml' so that the Concept Scheme remains on its own level,
        # rather than inside one of the concepts.
        return graph.serialize(format='xml')


class ModelRdfResource(ModelResource):
    scheme = None
    vocabulary_filter = Q(vocabulary_status=ControlledVocabulary.CURRENT)

    class Meta:
        max_limit = 0
        detail_uri_name = 'term'
        serializer = RdfSerializer()

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<term>[\w\.-]+)/$' % self._meta.resource_name,
                self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]

    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.
        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = (
            self.serialize(request, data, desired_format,
                           options={'scheme': self.scheme}))

        return (response_class(content=serialized,
                               content_type=build_content_type(desired_format),
                               **response_kwargs))
