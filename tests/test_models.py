#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-bcm
------------

Tests for `django-bcm` models module.
"""

from django.test import TestCase

from bcm import models


class TestCompany(TestCase):

    def setUp(self):
        self.company = models.Company.objects.create(
            companyname='Test AG', shortname='Test_AG')

    def test_string_representation(self):
        self.assertEqual(str(self.company), self.company.companyname)

    def test_get_absolute_url(self):
        self.assertEqual(self.company.get_absolute_url(), '/company/1/')

    def tearDown(self):
        pass


class TestPerson(TestCase):

    def setUp(self):
        self.person = models.Person.objects.create(
            first_name="Max", last_name="Mustermann")

    def test_string_representation(self):
        self.assertEqual(str(self.person), self.person.fullname)

    def test_fullname(self):
        self.assertEqual("Max Mustermann", self.person.fullname)

    def test_get_absolute_url(self):
        self.assertEqual(self.person.get_absolute_url(), '/person/1/')

    def tearDown(self):
        pass
