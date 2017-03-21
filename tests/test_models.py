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
        pass

    def test_string_representation(self):
        company = models.Company(companyname="Test AG")
        self.assertEqual(str(company), company.companyname)

    def tearDown(self):
        pass
