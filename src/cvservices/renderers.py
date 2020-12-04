from rest_framework import renderers


class RDFRenderer(renderers.BaseRenderer):
    media_type = 'application/rdf+xml'
    format = 'skos'

    def render(self, data, media_type=None, renderer_context=None):
        return "This is SKOS DATA"


class CSVRenderer(renderers.BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'

    def render(self, data, media_type=None, renderer_context=None):
        return "This is CSV DATA"
