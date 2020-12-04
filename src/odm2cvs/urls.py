from typing import List

from django.urls import path, reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

from cvservices.views import api_list_views
from cvinterface.views.base_views import UnitsListView
from cvinterface.views.request_views import RequestsView, request_list_views, request_create_views, request_update_views
from cvinterface.views.vocabulary_views import VocabulariesView, list_views, detail_views

urlpatterns: List[path] = [
    path('', VocabulariesView.as_view(), name='home'),
    path('units/', UnitsListView.as_view(), name='units'),
    path('requests/', RequestsView.as_view(), name='requests_list'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='cvinterface/account/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
]

# cv list views
for cv_name, view in list_views.items():
    urlpatterns += [
        path(f'{cv_name}/', view, name=cv_name),
    ]

# cv detail views
for cv_name, view in detail_views.items():
    urlpatterns += [
        path(f'{cv_name}/<slug:term>/', view, name=f'{cv_name}_detail'),
        path(f'{cv_name}/<slug:term>/<int:pk>', view, name=f'{cv_name}_detail')
    ]

# request list views
for cv_name, view in request_list_views.items():
    urlpatterns += [
        path(f'requests/{cv_name}/', view, name=f'{cv_name}request'),
    ]

# request create views
for cv_name, view in request_create_views.items():
    urlpatterns += [
        path(f'requests/{cv_name}/new/', view, name=f'{cv_name}request_form'),
        path(f'requests/{cv_name}/new/<int:vocabulary_id>', view, name=f'{cv_name}request_form'),
    ]

# request update views
for cv_name, view in request_update_views.items():
    urlpatterns += [
        path(f'requests/{cv_name}/<int:vocabulary_id>/', view, name=f'{cv_name}request_update_form'),
    ]


# api list views
for cv_name, api_view in api_list_views.items():
    urlpatterns += format_suffix_patterns([
        path(f'api/v1/{cv_name}/', api_view, name=f'{cv_name}_api_list')
    ])
