from typing import List

from django.urls import path, reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views import View
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView

from cvservices.views import api_views, UnitsAPIView
from cvinterface.views.base_views import UnitsListView
from cvinterface.views.request_views import RequestsView, request_list_views, request_create_views, request_update_views
from cvinterface.views.vocabulary_views import VocabulariesView, list_views, detail_views
from odm2cvs.controlled_vocabularies import vocabularies, VocabularyRequest

urlpatterns: List[path] = [
    path('', VocabulariesView.as_view(), name='home'),
    path('units/', UnitsListView.as_view(), name='units'),
    path('requests/', RequestsView.as_view(), name='requests_list'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='cvinterface/account/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += format_suffix_patterns([
    path('api/v1/units/', UnitsAPIView.as_view(), name='units_list_api')
])

for vocabulary_code, vocabulary in vocabularies.items():
    request: VocabularyRequest = vocabulary.get('request')

    list_view: View = list_views.get(vocabulary_code)
    detail_view: View = detail_views.get(vocabulary_code)
    request_list_view: View = request_list_views.get(vocabulary_code)
    request_create_view: View = request_create_views.get(vocabulary_code)
    request_update_view: View = request_update_views.get(vocabulary_code)
    api_view: APIView = api_views.get(vocabulary_code)

    # cv list views
    urlpatterns += [
        path(f'{vocabulary_code}/', list_view, name=vocabulary.get('list_url_name')),
    ]

    # cv detail views
    urlpatterns += [
        path(f'{vocabulary_code}/<slug:term>/', detail_view, name=vocabulary.get('detail_url_name')),
        path(f'{vocabulary_code}/<slug:term>/<int:pk>', detail_view, name=vocabulary.get('detail_url_name'))
    ]

    # request list views
    urlpatterns += [
        path(f'requests/{vocabulary_code}/', request_list_view, name=request.get('list_url_name')),
    ]

    # request create views
    urlpatterns += [
        path(f'requests/{vocabulary_code}/new/', request_create_view, name=request.get('create_url_name')),
        path(f'requests/{vocabulary_code}/new/<int:vocabulary_id>', request_create_view, name=request.get('create_url_name')),
    ]

    # request update views
    urlpatterns += [
        path(f'requests/{vocabulary_code}/<int:vocabulary_id>/', request_update_view, name=request.get('update_url_name')),
    ]

    # api views
    urlpatterns += format_suffix_patterns([
        path(f'api/v1/{vocabulary_code}/', api_view, name=vocabulary.get('api_list_url_name')),
        path(f'api/v1/{vocabulary_code}/<slug:term>', api_view, name=vocabulary.get('api_detail_url_name'))
    ])
