import sqlite3

from flask import current_app, g
from werkzeug.security import generate_password_hash

import os

DATABASE_PATH=os.path.join('instance', 'connectior.sqlite')

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


def create_db():
    db = get_db()

    with current_app.open_resource(os.path.join('static', 'sql', 'schema.sql')) as f:
        db.executescript(f.read().decode('utf8'))

def delete_db():
    if os.path.exists(current_app.config['DATABASE']):
        os.remove(current_app.config['DATABASE'])


def create_db_command():
    """Clear the existing data and create new tables."""
    create_db()
    print('Successfully create database.')



def fill_db_command():
    """Fill the database with test data."""
    db = get_db()

    with current_app.open_resource(os.path.join('static', 'sql', 'schema-fill.sql')) as f:
        db.executescript(f.read().decode('utf8'))

    users = db.execute('SELECT id, password FROM users').fetchall()

    for user in users:
        # Hash the password
        hashed_password = generate_password_hash(user['password'])

        # Update the user record with the hashed password
        db.execute('UPDATE users SET password = ? WHERE id = ?', (hashed_password, user['id']))
    
    db.commit()

    print('Successfully fill the database with test data.')


def delete_db_command():
    """Delete database file if exist"""

    delete_db()

    print('Successfully deleted database file.')


def reset_db_command():
    """Delete old database file and create a new one."""

    delete_db()
    create_db()

    print('Succesfully reset database')

def init_app(app):
    app.teardown_appcontext(close_db)
