from django.urls import include, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import reverse_lazy

from src.odm2cvs.cvinterface.views.base_views import UnitsListView
from src.odm2cvs.cvservices.api import v1_api
from src.odm2cvs.cvinterface.controlled_vocabularies import requests
from src.odm2cvs.cvinterface.views.vocabulary_views import VocabulariesView, list_views, detail_views
from src.odm2cvs.cvinterface.views.request_views import RequestsView, \
    request_list_views, request_create_views, request_update_views


logout_configuration = {
    'next_page': reverse_lazy('home')
}

urlpatterns = [
    re_path(r'^' + settings.SITE_URL + '$', VocabulariesView.as_view(), name='home'),
    re_path(r'^' + settings.SITE_URL + 'api/', include(v1_api.urls)),
    re_path(r'^' + settings.SITE_URL + 'admin/', include(admin.site.urls)),
    re_path(r'^' + settings.SITE_URL + 'units/', UnitsListView.as_view(), name='units'),
    re_path(r'^' + settings.SITE_URL + 'requests/$', RequestsView.as_view(), name='requests_list'),
    re_path(r'^' + settings.SITE_URL + 'login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^' + settings.SITE_URL + 'logout/$', auth_views.LogoutView.as_view(), logout_configuration, name='logout'),
]


# cv list views
for cv_name in list_views:
    view = list_views[cv_name]

    urlpatterns += [
        re_path(r'^' + settings.SITE_URL + cv_name + '/$', view, name=cv_name),
    ]

# cv detail views
for cv_name in detail_views:
    view = detail_views[cv_name]

    urlpatterns += [
        re_path(r'^' + settings.SITE_URL + cv_name + '/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$', view, name=cv_name + '_detail'),
    ]
    urlpatterns += [
        re_path(r'^' + settings.SITE_URL + cv_name + '/(?P<slug>[-\w]+)/$', view, name=cv_name + '_detail'),
    ]


# request list views
for request_name in request_list_views:
    view = request_list_views[request_name]

    urlpatterns += [
        re_path(r'^' + settings.SITE_URL + 'requests/' + requests[request_name]['vocabulary'] + '/$', view,
            name=request_name),
    ]

# request create views
for request_name in request_create_views:
    view = request_create_views[request_name]
    urlpatterns += [
        re_path(r'^' + settings.SITE_URL + 'requests/' + requests[request_name]['vocabulary'] + '/new/$', view,
            name=requests[request_name]['vocabulary'] + '_form'),
        re_path(r'^' + settings.SITE_URL + 'requests/' + requests[request_name]['vocabulary'] + '/new/(?P<vocabulary_id>[\w]+)/$',
            view, name=requests[request_name]['vocabulary'] + '_form'),
    ]

# request update views
for request_name in request_update_views:
    view = request_update_views[request_name]

    urlpatterns += [
        re_path(r'^' + settings.SITE_URL + 'requests/' + requests[request_name]['vocabulary'] + '/(?P<pk>[-\w]+)/$', view,
            name=requests[request_name]['vocabulary'] + '_update_form'),
    ]
