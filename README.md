# FAB Quick Start Utility - build `views.py`
The `fab-quick-start` command line utility generates
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder)
`views.py` files, to create instant multi-page, multi-table apps.

Use this [FAB Quick Start Guide](https://github.com/valhuber/fab-quick-start/wiki) to create the application below in 10 minutes.

## Features
Generated fab pages look as shown below:
1. __Multi-page:__ apps incude 1 page per table
1. __Multi-table:__ pages include `related_views` for each related child table, and join in parent data
1. __Favorite field first:__ first-displayed field is "name", or _contains_ "name" (configurable)
1. __Predictive joins:__ favorite field of each parent is shown (product _name_ - not product _id_)
1. __Ids last:__ such boring fields are not shown on lists, and at the end on other pages

![generated page](https://drive.google.com/uc?export=view&id=1Q3cG-4rQ6Q6RdZppvkrQzCDhDYHnk-F6)


## Background
[Flask Application Builder (FAB)](https://github.com/dpgaspar/Flask-AppBuilder) provides a rapid means for building web pages for database apps, based on Python, Flask and sqlalchemy.  Use this [Quick Start Guide](https://github.com/valhuber/fab-quick-start/wiki) to create the application above in 10 minutes.


Recall that creating the `views.py` file can be [tedious](https://github.com/valhuber/fab-quick-start/wiki#key-fab-inputs-modelspy-and-viewspy).  This utility generates the `views.py` file from the `models.py` file, to save time and reduce learning curve.


## Usage
First, create a fab project (e.g., see the Quick Start Guide).

Then, generate the `views.py` file like this:

```
cd <project>  # fab directory containing `config.py` file
pip install -i https://test.pypi.org/simple/ fab-quick-start

fab-quick-start
```

Copy the console output to your `views.py` file, and run fab / flask app:

```
export FLASK_APP=app
flask run
```



***
## Explore fab-quick-start
Use this to [explore the FAB Quick Start Utility](https://github.com/valhuber/fab-quick-start/wiki/Explore-fab_quick-start).
