# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Company,
	Person,
	Group,
)


class CompanyCreateView(CreateView):

    model = Company


class CompanyDeleteView(DeleteView):

    model = Company


class CompanyDetailView(DetailView):

    model = Company


class CompanyUpdateView(UpdateView):

    model = Company


class CompanyListView(ListView):

    model = Company


class PersonCreateView(CreateView):

    model = Person


class PersonDeleteView(DeleteView):

    model = Person


class PersonDetailView(DetailView):

    model = Person


class PersonUpdateView(UpdateView):

    model = Person


class PersonListView(ListView):

    model = Person


class GroupCreateView(CreateView):

    model = Group


class GroupDeleteView(DeleteView):

    model = Group


class GroupDetailView(DetailView):

    model = Group


class GroupUpdateView(UpdateView):

    model = Group


class GroupListView(ListView):

    model = Group

