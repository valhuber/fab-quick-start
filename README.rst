FAB Quick Start Utility - build ``views.py``
============================================

The ``fab-quickstart`` command line utility creates the
`Flask App Builder <https://github.com/dpgaspar/Flask-AppBuilder>`_ ``views.py`` file,
directly from ``models.py``, for an instant multi-page, multi-table app.

Use this `FAB Quick Start Guide <https://github.com/valhuber/fab-quickstart/wiki>`_ 
to create the app shown below in 10 minutes.


Features
--------

Generated fab pages look as shown below:

#. **Multi-page:** apps incude 1 page per table

#. **Multi-table:** pages include ``related_views`` for each related child table, and join in parent data

#. **Favorite field first:** first-displayed field is "name", or `contains` "name" (configurable)

#. **Predictive joins:** favorite field of each parent is shown (product _name_ - not product _id_)

#. **Ids last:** such boring fields are not shown on lists, and at the end on other pages

.. image:: https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6

Background:
-----------

Flask Application Builder (FAB) provides a rapid means for
building web pages for database apps, based on Python, Flask and sqlalchemy.
Use the Quick Start Guide (link above) to create the application
shown above in 10 minutes.

Recall that creating the ``views.py`` file can be
`tedious. <https://github.com/valhuber/fab-quickstart/wiki#key-fab-inputs-modelspy-and-viewspy>`_
This utility generates the ``views.py`` file from the ``models.py`` file,
to save time and reduce learning curve.

Usage:
------
First, create a fab project (e.g., see the Quick Start Guide).

Then, generate the ``views.py`` file like this::

    cd <project>  # fab directory containing the config.py file
    pip install -i https://test.pypi.org/simple/ FAB-Quickstart
    
    fab-quickstart

Copy the console output to your `views.py` file, and run fab / flask app::

    export FLASK_APP=app
    flask run

Depends on:
-----------
- Flask-AppBuilder

More information:
-----------------
The `FAB Quick Start github <https://github.com/valhuber/fab-quickstart#fab-quick-start---build-viewspy>`_ for more information, and explore the code.




Change Log
----------

Initial Version
