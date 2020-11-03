from operator import itemgetter

from django.urls import reverse
from django.views.generic import ListView

from cvinterface.views.base_views import DefaultVocabularyListView, DefaultVocabularyDetailView
from odm2cvs.controlled_vocabularies import vocabularies

defaults = {
    'list_view': DefaultVocabularyListView,
    'detail_view': DefaultVocabularyDetailView,
    'list_template': 'cvinterface/vocabularies/default_list.html',
    'detail_template': 'cvinterface/vocabularies/default_detail.html'
}


list_views = {}
detail_views = {}

for vocabulary_code, vocabulary in vocabularies.items():
    # list view
    list_views[vocabulary_code] = vocabulary.get('list_view', defaults['list_view']).as_view(
        vocabulary=vocabulary, vocabulary_code=vocabulary_code,
        template_name=vocabulary.get('list_template', defaults['list_template'])
    )

    # detail view
    detail_views[vocabulary_code] = vocabulary.get('list_view', defaults['detail_view']).as_view(
        vocabulary=vocabulary_code, vocabulary_verbose=vocabulary.get('name'),
        model=vocabulary.get('model'), template_name=vocabulary.get('detail_template', defaults['detail_template'])
    )


class VocabulariesView(ListView):
    queryset = []
    template_name = 'cvinterface/index.html'

    def get_context_data(self, **kwargs):
        context = super(VocabulariesView, self).get_context_data(**kwargs)

        vocabulary_types = [{'name': vocabulary.get('name'),
                             'definition': vocabulary.get('description'),
                             'url': reverse(vocabulary_name)}
                            for vocabulary_name, vocabulary in vocabularies.items()]

        context['vocabulary_views'] = sorted(vocabulary_types, key=itemgetter('name'))
        return context
