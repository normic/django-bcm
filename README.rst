=============================
Django Business Contact Manager
=============================

.. image:: https://badge.fury.io/py/django-bcm.svg
    :target: https://badge.fury.io/py/django-bcm

.. image:: https://travis-ci.org/normic/django-bcm.svg?branch=master
    :target: https://travis-ci.org/normic/django-bcm

.. image:: https://codecov.io/gh/normic/django-bcm/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/normic/django-bcm

A Django powered Manager for (mainly) business contacts.

Documentation
-------------

The full documentation is at https://django-bcm.readthedocs.io.

Quickstart
----------

Install Django Business Contact Manager::

    pip install django-bcm

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'bcm.apps.BCMConfig',
        ...
    )

Add Django Business Contact Manager's URL patterns:

.. code-block:: python

    from bcm import urls as bcm_urls


    urlpatterns = [
        ...
        url(r'^', include(bcm_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
