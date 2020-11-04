from operator import itemgetter

from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from django.utils.decorators import method_decorator
from django.views.generic import ListView

from cvinterface.views.base_views import DefaultRequestListView, DefaultRequestCreateView, DefaultRequestUpdateView
from odm2cvs.controlled_vocabularies import vocabularies

defaults = {
    'list_view': DefaultRequestListView,
    'create_view': DefaultRequestCreateView,
    'update_view': DefaultRequestUpdateView,
    'list_template': 'cvinterface/requests/default_list.html',
    'create_template': 'cvinterface/requests/default_form.html',
    'update_template': 'cvinterface/requests/default_update_form.html'
}

request_list_views = {}
request_create_views = {}
request_update_views = {}

for vocabulary_code, vocabulary in vocabularies.items():
    request = vocabulary.get('request')

    # list view
    request_list_views[vocabulary_code] = request.get('list_view', defaults['list_view']).as_view(
        vocabulary=vocabulary, vocabulary_code=vocabulary_code,
        template_name=request.get('list_template', defaults['list_template'])
    )

    # create_view
    request_create_views[vocabulary_code] = request.get('create_view', defaults['create_view']).as_view(
        request_name=f'{vocabulary_code}request', model=request.get('model'),
        vocabulary=vocabulary_code, request_verbose=request.get('name'),
        template_name=request.get('create_template', defaults['create_template']),
        vocabulary_verbose=vocabulary.get('name'), vocabulary_model=vocabulary.get('model')
    )

    # update view
    request_update_views[vocabulary_code] = request.get('update_view', defaults['update_view']).as_view(
        vocabulary=vocabulary, vocabulary_code=vocabulary_code,
        template_name=request.get('update_template', defaults['update_template'])
    )


class RequestsView(ListView):
    queryset = []
    template_name = 'cvinterface/requests/main_requests_list.html'
    
    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, *args, **kwargs):
        return super(RequestsView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        requests_list = [{'name': vocabulary.get('request').get('name'),
                          'url': reverse(f'{vocabulary_name}request'),
                          'vocabulary': vocabulary.get('name')}
                         for vocabulary_name, vocabulary in vocabularies.items()]

        pending_requests = [(pending_object, pending_object._meta.verbose_name, f'{vocabulary_name}request_update_form')
                            for vocabulary_name, vocabulary in vocabularies.items()
                            for pending_object in vocabulary.get('request').get('model').objects.filter(status='Pending')
                            if vocabulary.get('request').get('model').objects.filter(status='Pending').count() > 0]

        context['requests'] = sorted(requests_list, key=itemgetter('name'))
        context['pending_requests'] = pending_requests

        return context
