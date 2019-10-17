=============================
django-exporter
=============================

.. image:: https://badge.fury.io/py/django-exporter.svg
    :target: https://badge.fury.io/py/django-exporter

.. image:: https://travis-ci.org/shashisp/django-exporter.svg?branch=master
    :target: https://travis-ci.org/shashisp/django-exporter

.. image:: https://codecov.io/gh/shashisp/django-exporter/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/shashisp/django-exporter

Description 

Documentation
-------------

The full documentation is at https://django-exporter.readthedocs.io.

Quickstart
----------

Install django-exporter::

    pip install django-exporter

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_exporter.apps.DjangoExporterConfig',
        ...
    )

Add django-exporter's URL patterns:

.. code-block:: python

    from django_exporter import urls as django_exporter_urls


    urlpatterns = [
        ...
        url(r'^', include(django_exporter_urls)),
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
