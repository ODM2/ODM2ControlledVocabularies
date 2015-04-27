from operator import itemgetter

from cvinterface.views.base_views import *
from cvinterface.control_vocabularies import vocabularies, vocabulary_list_view, vocabulary_list_template, \
    vocabulary_detail_view, vocabulary_detail_template


list_views = {}
for cv_name in vocabularies:
    vocabulary = vocabularies[cv_name]
    view = vocabulary['list_view'] if 'list_view' in vocabulary else vocabulary_list_view
    template = vocabulary['list_template'] if 'list_template' in vocabulary else vocabulary_list_template
    list_views[cv_name] = view.as_view(vocabulary=cv_name, vocabulary_def=vocabulary['definition'], vocabulary_verbose=vocabulary['name'],
        model=vocabulary['model'], template_name=template,
    )


detail_views = {}
for cv_name in vocabularies:
    vocabulary = vocabularies[cv_name]
    view = vocabulary['detail_view'] if 'detail_view' in vocabulary else vocabulary_detail_view
    template = vocabulary['detail_template'] if 'detail_template' in vocabulary else vocabulary_detail_template

    detail_views[cv_name] = view.as_view(vocabulary=cv_name, vocabulary_verbose=vocabulary['name'],
        model=vocabulary['model'], template_name=template,
    )


class VocabulariesView(ListView):
    queryset = []
    template_name = 'cvinterface/index.html'

    def get_context_data(self, **kwargs):
        context = super(VocabulariesView, self).get_context_data(**kwargs)

        vocabulary_types = [{'name': vocabularies[vocabulary_name]['name'],
                             'definition': vocabularies[vocabulary_name]['definition'],
                             'url': reverse(vocabulary_name)}
                            for vocabulary_name in vocabularies]

        context['vocabulary_views'] = sorted(vocabulary_types, key=itemgetter('name'))
        return context
