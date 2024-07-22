from flask import Blueprint
from threading import Lock
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

bp = Blueprint('messanger', __name__)

app = Flask(__name__)
socketio = SocketIO(app)
thread = None
thread_lock = Lock()


@bp.route('/messanger')
def messanger():
    return render_template("messanger.html")
