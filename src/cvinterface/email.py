from typing import Dict

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.core.mail import send_mail
from django.forms import Form
from django.template.loader import render_to_string
from django.urls import reverse

from odm2cvs.controlled_vocabularies import Vocabulary

email_map: Dict[str, Dict[str, Dict[str, str]]] = {
    'request_made': {
        'admin': {
            'subject': 'cvinterface/email/request_made/subject_admin.tpl',
            'body': 'cvinterface/email/request_made/body_admin.tpl'
        },
        'user': {
            'subject': 'cvinterface/email/request_made/subject_user.tpl',
            'body': 'cvinterface/email/request_made/body_user.tpl'
        }
    },
    'update_approved': {
        'user': {
            'subject': 'cvinterface/email/update_approved/subject.tpl',
            'body': 'cvinterface/email/update_approved/body.tpl'
        }
    },
    'update_rejected': {
        'user': {
            'subject': 'cvinterface/email/update_rejected/subject.tpl',
            'body': 'cvinterface/email/update_rejected/body.tpl'
        }
    }
}


class EmailHandler:
    def __init__(self, web_form: Form, web_request: WSGIRequest, vocabulary: Vocabulary, email_type: str, receiver: str):
        self.form = web_form
        self.web_request = web_request
        self.vocabulary = vocabulary
        self.email_type = email_type
        self.email_receiver = receiver
        self.recipients = {
            'user': [self.form.instance.submitter_email],
            'admin': settings.EMAIL_RECIPIENTS
        }

    def get_email_context(self) -> Dict[str, str]:
        return {
            'submitter_name': self.form.instance.submitter_name,
            'submitter_email': self.form.instance.submitter_email,
            'concept_name': self.form.instance.name,
            'concept_term': self.form.instance.term,
            'concept_notes': self.form.instance.note,
            'concept_definition': self.form.instance.definition,
            'request_reason': self.form.instance.request_reason,
            'vocabulary_verbose_name': self.vocabulary.get('name'),
            'action': 'creation of a new ' if not self.form.instance.request_for_id else 'update of a ',
            'vocabulary_list_url': self.web_request.build_absolute_uri(reverse(self.vocabulary.get('list_url_name'))),
            'requests_list_url': self.web_request.build_absolute_uri(reverse('requests_list'))
        }

    def send_email(self):
        context: Dict[str, str] = self.get_email_context()
        email: Dict[str, str] = email_map.get(self.email_type).get(self.email_receiver)

        subject: str = render_to_string(template_name=email.get('subject'))
        message: str = render_to_string(template_name=email.get('body'), context=context)
        send_mail(subject, message, settings.EMAIL_SENDER, self.recipients.get(self.email_receiver), fail_silently=True)


def notify_update_approved(sender: Form, **kwargs) -> None:
    """
    Handler to send email to users when their request has been approved by an administrator.
    :param sender: The signal sender, in this case the django form object.
    :param kwargs: Dict with metadata for the request being approved.
    :return:
    """
    email_handler = EmailHandler(sender, kwargs.get('web_request'), kwargs.get('vocabulary'), 'update_approved', 'user')
    email_handler.send_email()


def notify_update_rejected(sender: Form, **kwargs) -> None:
    """
    Handler to send email to users when their request has been refused by an administrator.
    :param sender: The signal sender, in this case the django form object.
    :param kwargs: Dict with the vocabulary and vocabulary code of the request being refused.
    :return:
    """

    email_handler = EmailHandler(sender, kwargs.get('web_request'), kwargs.get('vocabulary'), 'update_rejected', 'user')
    email_handler.send_email()


def notify_admin_request_made(sender: Form, **kwargs) -> None:
    """
    Handler to send email to administrators when a request has been made by a user.
    :param sender: The signal sender, in this case the django form object.
    :param kwargs: Dict with the vocabulary and vocabulary code of the request being made.
    :return:
    """

    email_handler = EmailHandler(sender, kwargs.get('web_request'), kwargs.get('vocabulary'), 'request_made', 'admin')
    email_handler.send_email()


def notify_user_request_made(sender: Form, **kwargs) -> None:
    """
    Handler to send a confirmation email to a user who just requested a new term.
    :param sender: The signal sender, in this case the django form object.
    :param kwargs: Dict with the vocabulary and vocabulary code of the request being made.
    :return:
    """

    email_handler = EmailHandler(sender, kwargs.get('web_request'), kwargs.get('vocabulary'), 'request_made', 'user')
    email_handler.send_email()
