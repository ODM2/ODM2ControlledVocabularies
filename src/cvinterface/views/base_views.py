from typing import List

import requests

from os import linesep
from string import capwords
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy


# Vocabulary Basic Views
from cvinterface.signals import request_approved, request_rejected, request_made
from cvservices.models import ControlledVocabularyRequest, Unit
from odm2cvs.controlled_vocabularies import Vocabulary


class DefaultVocabularyListView(ListView):
    context_object_name: str = 'concepts_list'

    vocabulary: Vocabulary = {}
    vocabulary_code: str = ''

    def __init__(self, **kwargs):
        self.vocabulary_code = kwargs.get('vocabulary_code')
        self.vocabulary = kwargs.get('vocabulary')
        self.model = self.vocabulary.get('model')
        super(DefaultVocabularyListView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DefaultVocabularyListView, self).get_context_data(**kwargs)
        context['vocabulary_verbose_name'] = self.vocabulary.get('name')
        context['vocabulary_description'] = self.vocabulary.get('description')
        context['detail_url_name'] = self.vocabulary.get('detail_url_name')
        context['create_url'] = reverse(self.vocabulary.get('request').get('create_url_name'))
        context['api_url'] = reverse(self.vocabulary.get('api_list_url_name'))
        context['vocabulary_code'] = self.vocabulary_code
        return context

    def get_queryset(self):
        queryset = super(DefaultVocabularyListView, self).get_queryset()
        return queryset.filter(vocabulary_status=self.model.CURRENT)


class DefaultVocabularyDetailView(DetailView):
    exclude = ['name', 'definition', 'vocabulary_id', 'controlledvocabulary_ptr', 'vocabulary_status', 'previous_version']
    context_object_name: str = 'concept'
    pk_url_kwarg: str = 'vocabulary_id'
    query_pk_and_slug: bool = True
    slug_url_kwarg: str = 'term'
    slug_field: str = 'term'

    vocabulary: Vocabulary = {}
    vocabulary_code: str = ''

    def __init__(self, **kwargs):
        self.vocabulary_code = kwargs.get('vocabulary_code')
        self.vocabulary = kwargs.get('vocabulary')
        self.model = self.vocabulary.get('model')
        super(DefaultVocabularyDetailView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DefaultVocabularyDetailView, self).get_context_data(**kwargs)
        context['fields'] = tuple(
            (capwords(field.verbose_name), field.value_to_string(self.get_object()))
            for field in self.model._meta.fields
            if field.name not in self.exclude
        )
        context['vocabulary_verbose_name'] = self.vocabulary.get('name')
        context['detail_url_name'] = self.vocabulary.get('detail_url_name')
        context['edit_url'] = reverse(self.vocabulary.get('request').get('create_url_name'), args=(self.object.pk, ))
        context['api_url'] = reverse(self.vocabulary.get('api_detail_url_name'), args=(self.object.term, ))
        context['list_url'] = reverse(self.vocabulary.get('list_url_name'))
        context['vocabulary_code'] = self.vocabulary_code
        context['ARCHIVED'] = self.model.ARCHIVED
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        if u'pk' in self.kwargs:
            queryset = queryset.filter(pk=self.kwargs['pk'])
        else:
            queryset = queryset.filter(vocabulary_status=self.model.CURRENT)

        return super(DefaultVocabularyDetailView, self).get_object(queryset)


# Request Basic Views
class DefaultRequestListView(ListView, LoginRequiredMixin):
    context_object_name: str = 'requests_list'
    login_url = reverse_lazy('login')

    vocabulary: Vocabulary = {}
    vocabulary_code: str = ''

    def __init__(self, **kwargs):
        super(DefaultRequestListView, self).__init__(**kwargs)
        self.vocabulary_code = kwargs.get('vocabulary_code')
        self.vocabulary = kwargs.get('vocabulary')
        self.vocabulary_request = self.vocabulary.get('request')
        self.model = self.vocabulary_request.get('model')

    def get_context_data(self, **kwargs):
        context = super(DefaultRequestListView, self).get_context_data(**kwargs)
        context['vocabulary_verbose_name'] = self.vocabulary.get('name')
        context['request_verbose_name'] = self.vocabulary_request.get('name')
        context['update_url_name'] = self.vocabulary_request.get('update_url_name')
        context['vocabulary_list_url'] = reverse(self.vocabulary.get('list_url_name'))
        return context

    def get_queryset(self):
        queryset = super(DefaultRequestListView, self).get_queryset()
        return queryset.exclude(status=self.model.ARCHIVED)


class DefaultRequestUpdateView(UpdateView, LoginRequiredMixin, SuccessMessageMixin):
    exclude: List[str] = ['request_id', 'status', 'date_submitted', 'date_status_changed', 'request_for',
                          'original_request', 'submitter_name', 'submitter_email', 'subsequent_request']
    success_message: str = 'The request has been updated.'
    context_object_name: str = 'vocabulary_request'
    accept_button: str = 'request_accept'
    reject_button: str = 'request_reject'
    pk_url_kwarg: str = 'vocabulary_id'
    login_url = reverse_lazy('login')

    vocabulary: Vocabulary = {}
    vocabulary_code: str = ''

    def __init__(self, **kwargs):
        super(DefaultRequestUpdateView, self).__init__(**kwargs)
        self.vocabulary_code = kwargs.get('vocabulary_code')
        self.vocabulary = kwargs.get('vocabulary')
        self.request_code = f'{self.vocabulary_code}request'
        self.vocabulary_request = self.vocabulary.get('request')
        self.model = self.vocabulary_request.get('model')
        self.success_url = reverse(self.request_code)
        self.fields = [field.name for field in self.model._meta.fields if field.name not in self.exclude]

    def get_context_data(self, **kwargs):
        context = super(DefaultRequestUpdateView, self).get_context_data(**kwargs)
        context['all_disabled'] = self.object.status != ControlledVocabularyRequest.PENDING
        context['vocabulary_verbose_name'] = self.vocabulary.get('name')
        context['request_verbose_name'] = self.vocabulary_request.get('name')
        context['update_url_name'] = self.vocabulary_request.get('update_url_name')
        context['detail_url_name'] = self.vocabulary.get('detail_url_name')
        context['list_url'] = reverse(self.vocabulary_request.get('list_url_name'))
        context['success_view'] = 'request_success'
        return context

    def form_valid(self, form):
        if self.accept_button in self.request.POST:
            request_approved.send(sender=form, web_request=self.request, vocabulary=self.vocabulary)
            return self.accept_request(form)
        elif self.reject_button in self.request.POST:
            request_rejected.send(sender=form, web_request=self.request, vocabulary=self.vocabulary)
            return self.reject_request(form)

    def accept_request(self, form):
        vocabulary_model = self.vocabulary.get('model')
        updated_concept = vocabulary_model()

        is_editing_term = form.instance.request_for is not None
        vocabulary_fields = [term_field.name for term_field in updated_concept._meta.fields]
        request_fields = [request_field.name for request_field in form.instance._meta.fields]

        for field in vocabulary_fields:
            if field in request_fields:
                updated_concept.__setattr__(field, form.instance.__getattribute__(field))

        if is_editing_term:
            updated_concept.previous_version = form.instance.request_for
            form.instance.request_for.vocabulary_status = vocabulary_model.ARCHIVED
            form.instance.request_for.save()

        updated_concept.vocabulary_status = vocabulary_model.CURRENT
        updated_concept.save()

        revised_request = self.save_revised_request(form, ControlledVocabularyRequest.ACCEPTED)
        revised_request.request_for = updated_concept

        return super(DefaultRequestUpdateView, self).form_valid(form)

    def reject_request(self, form):
        self.save_revised_request(form, ControlledVocabularyRequest.REJECTED)
        return super(DefaultRequestUpdateView, self).form_valid(form)

    def save_revised_request(self, form, status):
        current_time = timezone.now()

        old_instance = self.model.objects.get(pk=form.instance.pk)
        old_instance.status = ControlledVocabularyRequest.ARCHIVED
        old_instance.date_status_changed = current_time
        old_instance.save()

        form.instance.pk = None
        form.instance.request_id = None
        form.instance.date_status_changed = current_time
        form.instance.original_request = old_instance
        form.instance.status = status
        form.instance.save()

        return form.instance


class DefaultRequestCreateView(SuccessMessageMixin, CreateView):
    exclude: List[str] = ['request_id', 'status', 'date_submitted', 'date_status_changed',
                          'request_for', 'request_notes', 'original_request']
    success_message: str = 'Your request has been made successfully.'
    context_object_name: str = 'vocabulary_request'
    pk_url_kwarg: str = 'vocabulary_id'
    login_url = reverse_lazy('login')

    submitter_fields = ['submitter_name', 'submitter_email', 'request_reason']
    recaptcha_key = settings.RECAPTCHA_KEY
    vocabulary: Vocabulary = {}
    vocabulary_code: str = ''

    def __init__(self, **kwargs):
        super(DefaultRequestCreateView, self).__init__(**kwargs)
        self.vocabulary_code = kwargs.get('vocabulary_code')
        self.vocabulary = kwargs.get('vocabulary')
        self.request_code = f'{self.vocabulary_code}request'
        self.vocabulary_request = self.vocabulary.get('request')
        self.model = self.vocabulary_request.get('model')
        self.success_url = reverse(self.vocabulary.get('list_url_name'))
        self.fields = [field.name for field in self.model._meta.fields if field.name not in self.exclude]

    def get_context_data(self, **kwargs):
        context = super(DefaultRequestCreateView, self).get_context_data(**kwargs)
        context['request_code'] = self.request_code
        context['vocabulary_verbose_name'] = self.vocabulary.get('name')
        context['request_verbose_name'] = self.vocabulary_request.get('name')
        context['vocabulary_code'] = self.vocabulary_code
        context['submitter_fields'] = self.submitter_fields
        context['recaptcha_user_key'] = settings.RECAPTCHA_USER_KEY
        return context

    def get_initial(self):
        if 'vocabulary_id' not in self.kwargs:
            return {}

        concept = self.vocabulary.get('model').objects.get(pk=self.kwargs.get('vocabulary_id'))
        initial_data = {field.name: concept.__getattribute__(field.name) for field in concept._meta.fields}
        return initial_data

    def is_captcha_valid(self, form):
        url = settings.RECAPTCHA_VERIFY_URL
        captcha_response = form.data.get('g-recaptcha-response')

        if not captcha_response:
            form.add_error(None, 'You are not human!!')
            return False

        params = urlencode({
            'secret': self.recaptcha_key,
            'response': captcha_response,
        })

        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'User-agent': 'reCAPTCHA Python'
        }

        captcha_request = requests.get(url, params, headers=headers)
        return captcha_request.json().get('success', False)

    def form_valid(self, form):
        if not self.is_captcha_valid(form):
            return super(DefaultRequestCreateView, self).form_invalid(form)

        if 'vocabulary_id' in self.kwargs:
            form.instance.request_for_id = self.kwargs.get('vocabulary_id')

        request_made.send(sender=form, web_request=self.request, vocabulary=self.vocabulary)
        return super(DefaultRequestCreateView, self).form_valid(form)


class UnitsListView(ListView):
    model = Unit
    template_name = 'cvinterface/units/list.html'


class UnitsDetailView(DetailView):
    model = Unit
    template_name = ''
    exclude = ['unit_id']
    slug_field = 'term'

