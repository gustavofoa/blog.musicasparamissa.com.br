Podcast
-------

This plugin generates plain-text or XML RSS podcasts. You can use the ``PODCAST``
variable in your settings file to configure the behavior of the plugin.

The ``PODCAST`` variable must be a Python dictionary and can contain these keys:

- ``title``, which is a dictionary with three keys:

- ``link``, which is a dictionary with three keys:

- ``language``, which is a dictionary with three keys:

- ``subtitle``, which is a dictionary with three keys:

- ``summary``, which is a dictionary with three keys:

- ``description``, which is a dictionary with three keys:

- ``author``, which is a dictionary with three keys:

- ``ownerName``, which is a dictionary with three keys:

- ``ownerEmail``, which is a dictionary with three keys:

- ``image``, which sets the URL for podcast image

If a key is missing or a value is incorrect, it will be replaced with the
default value.

You can also exclude an individual URL by adding metadata to it setting ``private``
to ``True``.

The sitemap is saved in ``<output_path>/sitemap.<format>``.

.. note::
   ``priorities`` and ``changefreqs`` are information for search engines.
   They are only used in the XML sitemaps.
   For more information: <http://www.sitemaps.org/protocol.html#xmlTagDefinitions>

**Example**

Here is an example configuration (it's also the default settings):

.. code-block:: python

    PLUGINS=['pelican.plugins.sitemap',]

    SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
        },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
        }
    }
