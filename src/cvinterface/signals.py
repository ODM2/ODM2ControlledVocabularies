import django.dispatch

from cvinterface.email import notify_approval, notify_refusal

# signal for when a request is created
request_submitted = django.dispatch.Signal()

# signal for when a request was rejected
request_rejected = django.dispatch.Signal()

# signal for when a request was rejected
request_approved = django.dispatch.Signal()


# signal handlers
request_approved.connect(notify_approval, dispatch_uid="cv_request_approved")
request_rejected.connect(notify_refusal, dispatch_uid="cv_request_rejected")
