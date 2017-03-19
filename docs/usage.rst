=====
Usage
=====

To use Django Business Contact Manager in a project, add it to your `INSTALLED_APPS`:

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
