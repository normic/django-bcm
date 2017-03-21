# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^Company/~create/$",
        view=views.CompanyCreateView.as_view(),
        name='Company_create',
    ),
    url(
        regex="^Company/(?P<pk>\d+)/~delete/$",
        view=views.CompanyDeleteView.as_view(),
        name='Company_delete',
    ),
    url(
        regex="^Company/(?P<pk>\d+)/$",
        view=views.CompanyDetailView.as_view(),
        name='Company_detail',
    ),
    url(
        regex="^Company/(?P<pk>\d+)/~update/$",
        view=views.CompanyUpdateView.as_view(),
        name='Company_update',
    ),
    url(
        regex="^Company/$",
        view=views.CompanyListView.as_view(),
        name='Company_list',
    ),
	url(
        regex="^Person/~create/$",
        view=views.PersonCreateView.as_view(),
        name='Person_create',
    ),
    url(
        regex="^Person/(?P<pk>\d+)/~delete/$",
        view=views.PersonDeleteView.as_view(),
        name='Person_delete',
    ),
    url(
        regex="^Person/(?P<pk>\d+)/$",
        view=views.PersonDetailView.as_view(),
        name='Person_detail',
    ),
    url(
        regex="^Person/(?P<pk>\d+)/~update/$",
        view=views.PersonUpdateView.as_view(),
        name='Person_update',
    ),
    url(
        regex="^Person/$",
        view=views.PersonListView.as_view(),
        name='Person_list',
    ),
	]
