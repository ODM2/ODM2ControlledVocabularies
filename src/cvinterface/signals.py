import django.dispatch

from cvinterface.email import notify_update_approved, notify_update_rejected, \
    notify_user_request_made, notify_admin_request_made

# signal for when a request is created
request_made = django.dispatch.Signal()

# signal for when a request was rejected
request_rejected = django.dispatch.Signal()

# signal for when a request was rejected
request_approved = django.dispatch.Signal()


# signal handlers
request_made.connect(notify_user_request_made, dispatch_uid='cv_request_made_user')
request_made.connect(notify_admin_request_made, dispatch_uid='cv_request_made_admin')
request_approved.connect(notify_update_approved, dispatch_uid='cv_request_approved')
request_rejected.connect(notify_update_rejected, dispatch_uid='cv_request_rejected')
