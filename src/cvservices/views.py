from typing import Tuple, Union, Dict, List

from django.db.models import QuerySet
from rest_framework.renderers import JSONRenderer, BaseRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from cvservices.models import ControlledVocabulary
from cvservices.renderers import CSVRenderer, RDFRenderer
from cvservices.serializers import VocabularySerializer
from odm2cvs.controlled_vocabularies import Vocabulary, vocabularies

api_list_views: Dict = {}
# api_detail_views = {}


class VocabularyConceptList(APIView):
    """
    API View for listing all concepts of one type of Controlled Vocabulary.
    """
    vocabulary_code: str = ''
    vocabulary: Vocabulary = {}
    renderer_classes: Tuple[BaseRenderer] = (JSONRenderer, CSVRenderer, RDFRenderer, )

    def get(self, request: Request, format: str = None) -> Response:
        vocabulary_serializer: VocabularySerializer = VocabularySerializer(many=True)
        queryset: QuerySet = self.vocabulary.get('model').objects.filter(vocabulary_status=ControlledVocabulary.CURRENT)
        serialized_vocabularies: Union[Dict, List] = vocabulary_serializer.to_representation(queryset)
        return Response(serialized_vocabularies)


for vocabulary_code, vocabulary in vocabularies.items():
    # api list views
    api_list_views[vocabulary_code] = VocabularyConceptList.as_view(
        vocabulary=vocabulary, vocabulary_code=vocabulary_code
    )
