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
)


class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'


class CompanyDeleteView(DeleteView):
    model = Company


class CompanyDetailView(DetailView):
    model = Company
    fields = '__all__'


class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'


class CompanyListView(ListView):
    model = Company
    fields = ('companyname', 'shortname')


class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'


class PersonDeleteView(DeleteView):
    model = Person
    fields = '__all__'


class PersonDetailView(DetailView):
    model = Person
    fields = '__all__'


class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'


class PersonListView(ListView):
    model = Person
    fields = '__str__'
