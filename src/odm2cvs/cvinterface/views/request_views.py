from operator import itemgetter

from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from src.odm2cvs.cvinterface.controlled_vocabularies import (
    request_create_template,
    request_create_view,
    request_list_template,
    request_list_view,
    request_update_template,
    request_update_view,
    requests,
    vocabularies,
)

request_list_views = {}
for request_name in requests:
    request = requests[request_name]
    vocabulary_name = vocabularies[request['vocabulary']]['name']
    view = request['list_view'] if 'list_view' in request else request_list_view
    template = request['list_template'] if 'list_template' in request else request_list_template

    request_list_views[request_name] = view.as_view(request=request_name, model=request['model'],
        vocabulary=request['vocabulary'], request_verbose=request['name'],
        template_name=template, vocabulary_verbose=vocabulary_name,
    )

request_create_views = {}
for request_name in requests:
    request = requests[request_name]
    vocabulary_name = vocabularies[request['vocabulary']]['name']
    view = request['create_view'] if 'create_view' in request else request_create_view
    template = request['create_template'] if 'create_template' in request else request_create_template

    request_create_views[request_name] = view.as_view(request_name=request_name, model=request['model'],
        vocabulary=request['vocabulary'], request_verbose=request['name'], template_name=template,
        vocabulary_model=request['vocabulary_model'], vocabulary_verbose=vocabulary_name,
    )

request_update_views = {}
for request_name in requests:
    request = requests[request_name]
    view = request['update_view'] if 'update_view' in request else request_update_view
    template = request['update_template'] if 'update_template' in request else request_update_template

    request_update_views[request_name] = view.as_view(request_name=request_name, model=request['model'],
        vocabulary=request['vocabulary'], request_verbose=request['name'], template_name=template,
        vocabulary_model=request['vocabulary_model']
    )


class RequestsView(ListView):
    queryset = []
    template_name = 'cvinterface/requests/main_requests_list.html'
    
    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, *args, **kwargs):
        return super(RequestsView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        requests_list = [{'name': requests[request_name]['name'], 'url': reverse(request_name),
                          'vocabulary': vocabularies[requests[request_name]['vocabulary']]['name']}
                         for request_name in requests]


        pending_requests = [(pending_object, pending_object._meta.verbose_name, requests[request_name]['vocabulary'] + '_update_form')
                            for request_name in requests
                            for pending_object in requests[request_name]['model'].objects.filter(status='Pending')
                            if requests[request_name]['model'].objects.filter(status='Pending').count() > 0]

        context['requests'] = sorted(requests_list, key=itemgetter('name'))
        context['pending_requests'] = pending_requests

        return context
