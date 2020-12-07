import csv
from ctypes import Union
from io import BytesIO, StringIO
from typing import Union, Dict, List, KeysView

from rest_framework import renderers


class RDFRenderer(renderers.BaseRenderer):
    media_type = 'application/rdf+xml'
    format = 'skos'

    def render(self, data, media_type=None, renderer_context=None):
        return "This is SKOS DATA"


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
