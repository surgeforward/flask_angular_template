import click
from werkzeug.serving import run_simple
from project.web import application
from project import settings
from project.manage.db import db
from project.manage.accounts import accounts


@click.group()
def cli():
    pass

cli.add_command(db)
cli.add_command(accounts)

@cli.command()
def runserver():
    run_simple('0.0.0.0', settings.PORT, application, use_reloader=settings.DEBUG, use_debugger=settings.DEBUG)

if __name__ == '__main__':
    cli()
