from typing import List

from django.urls import path, include, reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView

from cvservices.api import v1_api
from cvinterface.views import UnitsListView

from cvinterface import requests
from cvinterface.views import VocabulariesView, list_views, detail_views
from cvinterface.views import RequestsView, \
    request_list_views, request_create_views, request_update_views


urlpatterns: List[path] = [
    path('', VocabulariesView.as_view(), name='home'),
    path('api/', include(v1_api.urls)),
    path('admin/', include(admin.site.urls)),
    path('units/', UnitsListView.as_view(), name='units'),
    path('requests/', RequestsView.as_view(), name='requests_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='cvinterface/account/login.html',
        redirect_field_name='next'),
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page= reverse_lazy('home')), name='logout'),
]


# cv list views
cv_name: str

for cv_name in list_views:
    view: ListView = list_views[cv_name]

    urlpatterns += [
        path(f'{cv_name}/', view, name=cv_name),
    ]

# cv detail views
for cv_name in detail_views:
    view: DetailView = detail_views[cv_name]

    # TODO: find a django 3.1 equivalent of this slug + pk mess.
    urlpatterns += [
        path(f'{cv_name}/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$', view, name=cv_name + '_detail'),
    ]
    urlpatterns += [
        path(f'{cv_name}/(?P<slug>[-\w]+)/$', view, name=cv_name + '_detail'),
    ]


# request list views
for request_name in request_list_views:
    view = request_list_views[request_name]

    urlpatterns += [
        path(f'requests/{requests[request_name]["vocabulary"]}/', view, name=request_name),
    ]

# request create views
for request_name in request_create_views:
    view = request_create_views[request_name]
    urlpatterns += [
        path(f'requests/{requests[request_name]["vocabulary"]}/new/$', view,
            name=requests[request_name]['vocabulary'] + '_form'),
        # TODO: change vocabulary_id field here.
        path(f'requests/{requests[request_name]["vocabulary"]}/new/(?P<vocabulary_id>[\w]+)/$',
            view, name=requests[request_name]['vocabulary'] + '_form'),
    ]

# request update views
for request_name in request_update_views:
    view = request_update_views[request_name]

    urlpatterns += [
        # TODO: change pk here.
        path(f'requests/{requests[request_name]["vocabulary"]}/(?P<pk>[-\w]+)/$', view,
            name=requests[request_name]['vocabulary'] + '_update_form'),
    ]