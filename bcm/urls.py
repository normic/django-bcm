# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex="^company/create/$",
        view=views.CompanyCreateView.as_view(),
        name='company_create',
    ),
    url(
        regex="^company/(?P<pk>\d+)/delete/$",
        view=views.CompanyDeleteView.as_view(),
        name='company_delete',
    ),
    url(
        regex="^company/(?P<pk>\d+)/$",
        view=views.CompanyDetailView.as_view(),
        name='company_detail',
    ),
    url(
        regex="^company/(?P<pk>\d+)/update/$",
        view=views.CompanyUpdateView.as_view(),
        name='company_update',
    ),
    url(
        regex="^company/$",
        view=views.CompanyListView.as_view(),
        name='company_list',
    ),
    url(
        regex="^person/create/$",
        view=views.PersonCreateView.as_view(),
        name='person_create',
    ),
    url(
        regex="^person/(?P<pk>\d+)/delete/$",
        view=views.PersonDeleteView.as_view(),
        name='person_delete',
    ),
    url(
        regex="^person/(?P<pk>\d+)/$",
        view=views.PersonDetailView.as_view(),
        name='person_detail',
    ),
    url(
        regex="^person/(?P<pk>\d+)/update/$",
        view=views.PersonUpdateView.as_view(),
        name='person_update',
    ),
    url(
        regex="^person/$",
        view=views.PersonListView.as_view(),
        name='person_list',
    ),
]
