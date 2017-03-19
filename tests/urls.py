# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from bcm.urls import urlpatterns as bcm_urls

urlpatterns = [
    url(r'^', include(bcm_urls, namespace='bcm')),
]
