=====
Usage
=====

To use django-exporter in a project, add it to your `INSTALLED_APPS`:

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
