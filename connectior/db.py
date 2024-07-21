import sqlite3

import click
from flask import current_app, g, Blueprint

bp = Blueprint('database', __name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@bp.cli.command('init')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


@bp.cli.command('fill')
def fill_db_command():
    """Fill the database with test data."""
    db = get_db()

    with current_app.open_resource('schema-fill.sql') as f:
        db.executescript(f.read().decode('utf8'))

    click.echo('Filled the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)