import click
from base import FabQuickStart  # pip'd run fails - ModuleNotFoundError: No module named 'base'

@click.group()
def fab():
    """ FAB flask group commands"""
    pass


@fab.command("version")  # FIXME not working
def version():
    """
        FAB Quickstart package version
    """
    print("TODO - add version")
    click.echo(
        click.style(
            "F.A.B Version: {0}.".format(fab_quickstart.__version__),
            bg="blue",
            fg="white",
        )
    )

"""
    uploaded to https://test.pypi.org/project/FAB-Quickstart/0.9.0/
    so
        pip install -i https://test.pypi.org/simple/ FAB-Quickstart==0.9.0
        fabqs

    FIXME
        
        it runs!  but... for fab consistency... should it be??

        flask fab quickstart

"""
@click.command()
@click.option('--favorites',
              default="name description",
              prompt="Favorite Column Names",
              help="Word(s) used to identify 'favorite column' (displayed first)")
@click.option('--non_favorites',
              default="id",
              prompt="Non Favorite Column Names",
              help="Word(s) used to identify last-shown fields")
def main(favorites, non_favorites):
    """
        Creates instant web app - generates fab views contents.

\b
        fab is Flask Application Builder\r
            Docs:        https://flask-appbuilder.readthedocs.io/en/latest/\r
            Quick Start: https://github.com/valhuber/fab-quickstart

\b
        Usage\r
        =====\r
            1. Generate a fab project\r
            2. Complete your models file (consider sqlacodegen)\r
                https://pypi.org/project/sqlacodegen/\r
                NB: Add relationships missing in db to get related_views\r
            3. cd to directory containing your config.py file:\r
                cd my_project -- \r
                --app\r
                --|--__init__.py\r
                --|--models.py\r
                __|--views.py\r
                --config.py\r
            4. fab_quickstart\r
                dev mode\r
                    cd nw\r
                    python ../fab_quickstart/cli.py\r
            5. copy output over app/views.py
            6. cd my_project; flask run
    """
    fab_quick_start = FabQuickStart()
    fab_quick_start.favorite_names = favorites
    fab_quick_start.non_favorite_names = non_favorites
    fab_quick_start.run()

    print("\n" + fab_quick_start._result)


def start():
    print("\nFAB Quickstart Here\n")
    main(obj={})


if __name__ == '__main__':
    start()
