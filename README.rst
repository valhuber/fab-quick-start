FAB Quick Start Utility - build ``views.py``
============================================

The ``fab-quick-start`` command line utility creates the
`Flask App Builder <https://github.com/dpgaspar/Flask-AppBuilder>`_ ``views.py`` file,
directly from ``models.py``, for an instant multi-page, multi-table app.

Use this `FAB Quick Start Guide <https://github.com/valhuber/fab-quick-start/wiki>`_ 
to create the app shown below in 10 minutes.


Features
--------

Generated fab pages look as shown below:

#. **Multi-page:** apps incude 1 page per table

#. **Multi-table:** pages include ``related_views`` for each related child table, and join in parent data

#. **Favorite field first:** first-displayed field is "name", or `contains` "name" (configurable)

#. **Predictive joins:** favorite field of each parent is shown (product *name* - not product *id*)

#. **Ids last:** such boring fields are not shown on lists, and at the end on other pages

.. image:: https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6

Background:
-----------

Flask Application Builder (FAB) provides a rapid means for
building web pages for database apps, based on Python, Flask and sqlalchemy.
Use the Quick Start Guide (link above) to create the application
shown above in 10 minutes.

Recall that creating the ``views.py`` file can be
`tedious. <https://github.com/valhuber/fab-quick-start/wiki#key-fab-inputs-modelspy-and-viewspy>`_
This utility generates the ``views.py`` file from the ``models.py`` file,
to save time and reduce learning curve.

Usage:
------
First, create a fab project (e.g., see the Quick Start Guide).

Then, generate the ``views.py`` file like this::

    cd <project>  # fab directory containing the config.py file
    pip install fab-quick-start
    fab-quick-start run

Copy the console output to your `views.py` file, and run fab / flask app::

    export FLASK_APP=app
    flask run


Parameters
----------
The simple ``run`` command will request 2 parameters, and output to the console.
You can specify parameters and output via command line arguments, like this::

    fab-quick-start run --favorites="name description" --non_favorites="id" > app/views.py

where:

- **favorites:** words() used to find "favorite fields".  Fields named with these words,
  or *containing* these words, are placed at the *start* of lists and show pages.  
  Your values might reflect your language, and your database naming conventions.

- **non_favorites:** name(s) used to find fields to be place 
  at the *end* of list / show pages.

- the `>` pipes the output to a file (which is overwritten).


Depends on:
-----------
- Flask-AppBuilder


More information:
-----------------
The `FAB Quick Start github <https://github.com/valhuber/fab-quick-start#fab-quick-start-utility---build-viewspy>`_ for more information, and explore the code.


Acknowledgements
----------------
Many thanks to

- Daniel Vaz Gaspar, the creator of FAB, for his help and guidance

- Katrina Huber-Juma, for Python help and final review

- Tyler Band, for early testing



Change Log
----------

Initial Version

0.9.8 - Fix duplicate view class generation
