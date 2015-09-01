from django.http import HttpResponse

from tastypie.bundle import Bundle
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from tastypie.utils.mime import build_content_type

from .models import Scheme, Namespace, Node, FieldRelation

from rdflib import Graph, URIRef, Literal
from rdflib import Namespace as ns
from rdflib.namespace import SKOS, RDF

from collections import OrderedDict
import logging
import csv
import StringIO

class ModelRdfResource(ModelResource):
    scheme = None

    def create_response(self, request, data, response_class=HttpResponse,
                        **response_kwargs):
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



class RdfSerializer(Serializer):
    formats = ['json', 'skos', 'csv']
    content_types = {
        'json': 'application/json',
        #'skos': 'application/rdf+xml'
        'skos': 'text/plain',
        'csv': 'text/csv'
    }

    def to_csv(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        raw_data = StringIO.StringIO()
        
        first = True

        scheme = Scheme.objects.get(name=options['scheme'])
        
        # Entire CV
        if "meta" in data.keys():
            objects = data.get("objects")
            
            for value in objects:
                test = {}
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
                
                del test['resource_uri']
                
                odict.update(test)
                #odict['resource_uri'] = scheme.uri
                
                if first:

                    writer = csv.DictWriter(raw_data, odict.keys())
                    writer.writeheader()
                    writer.writerow(odict)
                    first = False
                else:
                    writer.writerow({k:(v.encode('utf-8') if isinstance(v, int) is not True else v) for k,v in odict.items()})
                    #writer.writerow(odict)
        # Single Term
        else:
            test = {}
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
            
            del test['resource_uri']

            odict.update(test)
            #odict['resource_uri'] = scheme.uri + "/" + odict['term']
            
            if first:
                writer = csv.DictWriter(raw_data, odict.keys())
                writer.writeheader()
                #writer.writerow(odict)
                writer.writerow({k:(v.encode('utf-8') if isinstance(v, int) is not True else v) for k,v in odict.items()})
                first = False
            else:
                writer.writerow(odict)
        
        csv_content = raw_data.getvalue()
        return csv_content

    def flatten(self, data, odict = {}):
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

        baseURI = 'http://vocabulary.odm2.org/ODM2/ODM2Terms/'
        graph = Graph()
        odm2 = ns(baseURI)
        dc = ns('http://purl.org/dc/elements/1.1/')

        graph.bind('odm2', odm2)
        graph.bind('skos', SKOS)
        graph.bind('dc', dc)

        # If requesting an entire CV.
        if isinstance(data, dict):
	    print data
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
                    if isinstance(label, int):
                        label = str(label)
                    # Skip resource_uri and term elements.
                    # TODO: remove these elements entirely?
                    if x == u'resource_uri' or x == 'term':
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
        # TODO: Return the Concept Scheme as well.
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
                if isinstance(label, int):
                    label = str(label)

                if field == 'term' or field == u'resource_uri':
                    continue
                elif label.rstrip('\r\n') == '':
                    continue
                else:
                    print "$$$$ field", field
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
