from uuid import uuid4
from string import capwords
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy


# Vocabulary Basic Views
from cvservices.models import ControlVocabularyRequest


class DefaultVocabularyListView(ListView):
    vocabulary = None
    vocabulary_verbose = None
    vocabulary_def = None

    def __init__(self, **kwargs):
        self.vocabulary = kwargs['vocabulary']
        self.vocabulary_verbose = kwargs['vocabulary_verbose']
        self.vocabulary_def = kwargs['vocabulary_def']
        super(DefaultVocabularyListView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DefaultVocabularyListView, self).get_context_data(**kwargs)
        context['vocabulary_verbose'] = self.vocabulary_verbose
        context['create_url'] = self.vocabulary + '_form'
        context['detail_url'] = self.vocabulary + '_detail'
        context['vocabulary_def'] = self.vocabulary_def
        context['vocabulary'] = self.vocabulary
        return context


class DefaultVocabularyDetailView(DetailView):
    vocabulary = None
    vocabulary_verbose = None
    exclude = ['term', 'name', 'definition']

    def __init__(self, **kwargs):
        super(DefaultVocabularyDetailView, self).__init__(**kwargs)
        self.vocabulary = kwargs['vocabulary']
        self.vocabulary_verbose = kwargs['vocabulary_verbose']


    def get_context_data(self, **kwargs):
        context = super(DefaultVocabularyDetailView, self).get_context_data(**kwargs)
        context['fields'] = dict((capwords(field.verbose_name), field.value_to_string(self.get_object())) for field in self.model._meta.fields if field.name not in self.exclude)
        context['vocabulary_verbose'] = self.vocabulary_verbose
        context['vocabulary'] = self.vocabulary
        context['create_url'] = self.vocabulary + '_form'
        return context


# Request Basic Views
class DefaultRequestListView(ListView):
    request = None
    vocabulary = None
    request_verbose = None

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, *args, **kwargs):
        return super(DefaultRequestListView, self).dispatch(*args, **kwargs)

    def __init__(self, **kwargs):
        super(DefaultRequestListView, self).__init__(**kwargs)
        self.request_verbose = kwargs['request_verbose']
        self.vocabulary = kwargs['vocabulary']
        self.request = kwargs['request']
        self.queryset = self.model.objects.filter(status=self.model.PENDING) \
                        | self.model.objects.filter(original_request__isnull=False)

    def get_context_data(self, **kwargs):
        context = super(DefaultRequestListView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['request_verbose'] = self.request_verbose
        context['update_url'] = self.vocabulary + '_update_form'
        return context


class DefaultRequestUpdateView(SuccessMessageMixin, UpdateView):
    request_name = None
    vocabulary = None
    vocabulary_model = None
    request_verbose = None
    accept_button = 'request_accept'
    reject_button = 'request_reject'
    success_message = 'The request has been updated.'
    exclude = ['request_id', 'term', 'status', 'date_submitted', 'date_status_changed', 'original_request']
    read_only = []

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, *args, **kwargs):
        return super(DefaultRequestUpdateView, self).dispatch(*args, **kwargs)

    def __init__(self, **kwargs):
        super(DefaultRequestUpdateView, self).__init__(**kwargs)
        self.request_name = kwargs['request_name']
        self.vocabulary = kwargs['vocabulary']
        self.vocabulary_model = kwargs['vocabulary_model']
        self.request_verbose = kwargs['request_verbose']
        self.success_url = reverse(self.request_name)
        self.fields = [field.name for field in self.model._meta.fields if field.name not in self.exclude]

    def get_context_data(self, **kwargs):
        context = super(DefaultRequestUpdateView, self).get_context_data(**kwargs)
        context['all_disabled'] = False if self.object.status == ControlVocabularyRequest.PENDING else True
        context['read_only'] = self.read_only
        context['request_name'] = self.request_name
        context['request_verbose'] = self.request_verbose
        context['update_url'] = self.vocabulary + '_update_form'
        context['vocabulary'] = self.vocabulary
        context['success_view'] = 'request_success'
        return context

    def post(self, request, *args, **kwargs):
        object = self.model.objects.get(pk=kwargs['pk'])
        request.POST._mutable = True
        for field in self.read_only:
            request.POST[field] = unicode(object.__getattribute__(field))
        return super(DefaultRequestUpdateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        if self.accept_button in self.request.POST:
            return self.accept_request(form)
        elif self.reject_button in self.request.POST:
            return self.reject_request(form)

    def accept_request(self, form):
        vocabulary_filter = self.vocabulary_model.objects.filter(pk=form.instance.pk)
        exists = vocabulary_filter.count() is 1
        concept = vocabulary_filter.get() if exists else self.vocabulary_model()

        concept_fields = [concept_field.name for concept_field in concept._meta.fields]
        request_fields = [request_field.name for request_field in form.instance._meta.fields]

        for field in concept_fields:
            if field in request_fields:
                concept.__setattr__(field, form.instance.__getattribute__(field))

        concept.save()
        self.save_and_duplicate_request(form, ControlVocabularyRequest.ACCEPTED)

        return super(DefaultRequestUpdateView, self).form_valid(form)

    def reject_request(self, form):
        self.save_and_duplicate_request(form, ControlVocabularyRequest.REJECTED)
        return super(DefaultRequestUpdateView, self).form_valid(form)

    def save_and_duplicate_request(self, form, status):
        new_request_id = uuid4()
        current_time = timezone.now()

        old_instance = self.model.objects.get(pk=form.instance.pk)
        old_instance.status = status
        old_instance.date_status_changed = current_time
        old_instance.save()

        form.instance.pk = new_request_id
        form.instance.id = new_request_id
        form.instance.status = status
        form.instance.date_status_changed = current_time
        form.instance.original_request = self.model.objects.get(pk=old_instance.pk)
        form.instance.save()


class DefaultRequestCreateView(SuccessMessageMixin, CreateView):
    request_name = None
    vocabulary = None
    request_verbose = None
    vocabulary_model = None
    vocabulary_verbose = None
    success_message = 'Your request has been made successfully.'
    exclude = ['request_id', 'status', 'date_submitted', 'date_status_changed', 'original_request', 'request_notes']

    def __init__(self, **kwargs):
        super(DefaultRequestCreateView, self).__init__(**kwargs)
        self.request_name = kwargs['request_name']
        self.vocabulary = kwargs['vocabulary']
        self.request_verbose = kwargs['request_verbose']
        self.vocabulary_model = kwargs['vocabulary_model']
        self.vocabulary_verbose = kwargs['vocabulary_verbose']
        self.success_url = reverse(self.vocabulary)
        self.fields = [field.name for field in self.model._meta.fields if field.name not in self.exclude]

    def get_context_data(self, **kwargs):
        context = super(DefaultRequestCreateView, self).get_context_data(**kwargs)
        context['request_name'] = self.request_name
        context['request_verbose'] = self.request_verbose
        context['vocabulary_verbose'] = self.vocabulary_verbose
        context['vocabulary'] = self.vocabulary
        context['term'] = self.kwargs['term'] if 'term' in self.kwargs else ''
        return context

    def get_initial(self):
        if 'term' not in self.kwargs:
            return {}

        concept_query = self.vocabulary_model.objects.filter(pk=self.kwargs['term'])
        if concept_query.count() is not 1:
            return {}

        initial_data = {}
        concept = concept_query.get()
        fields = [concept_field.name for concept_field in concept._meta.fields]
        for field in fields:
            initial_data[field] = concept.__getattribute__(field)

        return initial_data
