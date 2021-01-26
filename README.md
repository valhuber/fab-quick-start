# FAB Quick Start Utility - build `views.py`
The `fab-quick-start` command line utility generates
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder)
`views.py` files, to create instant multi-page, multi-table apps.

> **Update - Jan 26, 2021:** checkout [**ApiLogicServer**](https://github.com/valhuber/ApiLogicServer#readme) - create a complete JSON:API for your database, with LogicBank, and a basic web app


Use this [FAB Quick Start Guide](https://github.com/valhuber/fab-quick-start/wiki) to create the application below in 10 minutes.

## Features
Generated fab pages look as shown below:
1. __Multi-page:__ apps incude 1 page per table
1. __Multi-table:__ pages include `related_views` for each related child table, and join in parent data
1. __Favorite field first:__ first-displayed field is "name", or _contains_ "name" (configurable)
1. __Predictive joins:__ favorite field of each parent is shown (product _name_ - not product _id_)
1. __Ids last:__ such boring fields are not shown on lists, and at the end on other pages

<figure><img src="images/generated-page.png" width="800"></figure>


## Background
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder) provides a rapid means for building web pages for database apps, based on Python, Flask and sqlalchemy.  Use this [Quick Start Guide](https://github.com/valhuber/fab-quick-start/wiki) to create the application above in 10 minutes.


Recall that creating the `views.py` file can be [tedious](https://github.com/valhuber/fab-quick-start/wiki#key-fab-inputs-modelspy-and-viewspy).  This utility generates the `views.py` file from the `models.py` file, to save time and reduce learning curve.


## Usage (on your project)
First, create a fab project (e.g., see the Quick Start Guide).

Then, generate the `views.py` file like this:

```
cd <project>  # fab directory containing `config.py` file
pip install fab-quick-start
fab-quick-start run
```

Copy the console output to your `views.py` file, and run fab / flask app:

```
export FLASK_APP=app
flask run
```

## Parameters
The simple `run` command will request 2 parameters, and output to the console.
You can specify parameters and output via command line arguments, like this:
```
fab-quick-start run --favorites="name description" --non_favorites="id" > app/views.py
```
where
* __favorites:__ names()) used to find "favorite fields".  Fields named with these words, or
_containing_ these words, are placed at the _start_ of lists and show pages.  Your values might reflect your language, and your database naming conventions.
* __non_favorites:__ name(s) used to find fields to be placed at the _end_ of list / show pages.
* the `>` pipes the output to a file (which is overwritten).

## Foreign Keys
A key FAB service is automatic page navigations to see related data.
These depend on Foreign Key relationships.
Note statistics are shown in the last lines of the generated `view.py` file.

If they are not present, add them to your `models.py` file, or (better) to your schema.

***
## Explore fab-quick-start
To use this project:
```
git clone https://github.com/valhuber/fab-quick-start.git
cd fab-quick-start
virtualenv venv
source venv/bin/activate
cd nw/basic_web_app
export FLASK_APP=app
flask run
```

Use this to [explore the FAB Quick Start Utility further](https://github.com/valhuber/fab-quick-start/wiki/Explore-the-FAB-Quick-Start-Utility).

## Now with Logic
FAB works with [Logic Bank](https://github.com/valhuber/logicbank), which employs rules and Python to dramatically reduce and simplify backend code for business logic.

## Acknowledgements
Many thanks to
* Daniel Vaz Gaspar, the creator of FAB, for his help and guidance
* Katrina Huber-Juma, for Python help and final review
* Tyler Band, for early testing
* Achim Götz, for reporting a bug in examples

