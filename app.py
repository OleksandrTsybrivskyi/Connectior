import os

from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'connectior.sqlite'),
)
socketio = SocketIO(app)

os.makedirs(app.instance_path, exist_ok=True)

from lib import db
db.init_app(app)
app.register_blueprint(db.bp)

from lib import auth, messanger
app.register_blueprint(auth.bp)
app.register_blueprint(messanger.bp)
