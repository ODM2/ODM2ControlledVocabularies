from typing import Type, Dict

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.core.mail import send_mail
from django.forms import Form
from django.template.loader import render_to_string
from django.urls import reverse

from odm2cvs.controlled_vocabularies import Vocabulary

template_map: Dict[str, str] = {
    'update_subject': 'cvinterface/email/update_request_subject.tpl',
    'approved': 'cvinterface/email/update_approved_body.tpl',
    'rejected': 'cvinterface/email/update_rejected_body.tpl'
}


def get_email_context(web_form: Form, web_request: WSGIRequest, vocabulary: Vocabulary) -> Dict[str, str]:
    return {
        'submitter_name': web_form.instance.submitter_name,
        'concept_name': web_form.instance.name,
        'vocabulary_verbose_name': vocabulary.get('name'),
        'vocabulary_list_url': web_request.build_absolute_uri(reverse(vocabulary.get('list_url_name')))
    }


def notify_approval(sender: Form, **kwargs) -> None:
    """
    Handler to send email to users when their request has been approved by an administrator.
    :param sender: The signal sender, in this case the django form object.
    :param kwargs: Dict with the vocabulary and vocabulary code of the request being approved.
    :return:
    """

    email_context: Dict[str, str] = get_email_context(sender, kwargs.get('web_request'), kwargs.get('vocabulary'))
    email_message: str = render_to_string(template_name=template_map.get('approved'), context=email_context)
    email_subject: str = render_to_string(template_name=template_map.get('update_subject'))

    send_mail(email_subject, email_message, settings.EMAIL_SENDER, [sender.instance.submitter_email])


def notify_refusal(sender: Form, **kwargs) -> None:
    """
    Handler to send email to users when their request has been refused by an administrator.
    :param sender: The signal sender, in this case the django form object.
    :param kwargs: Dict with the vocabulary and vocabulary code of the request being refused.
    :return:
    """

    email_context: Dict[str, str] = get_email_context(sender, kwargs.get('web_request'), kwargs.get('vocabulary'))
    email_message: str = render_to_string(template_name=template_map.get('refused'), context=email_context)
    email_subject: str = render_to_string(template_name=template_map.get('update_subject'))

    send_mail(email_subject, email_message, settings.EMAIL_SENDER, [sender.instance.submitter_email])
