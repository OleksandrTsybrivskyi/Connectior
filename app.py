import os

from flask import Flask
from flask_socketio import SocketIO, emit

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from lib import db

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=db.DATABASE_PATH,
)
socketio = SocketIO(app)

os.makedirs(app.instance_path, exist_ok=True)


db.init_app(app)

from lib import auth, messanger
app.register_blueprint(auth.bp)
app.register_blueprint(messanger.bp)

@app.route('/')
def index():
    return redirect(url_for('auth.register'))
