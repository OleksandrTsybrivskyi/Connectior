from flask import Blueprint
from threading import Lock
from flask import Flask, render_template, session, url_for
from flask_socketio import SocketIO, emit

from lib.db import get_db

bp = Blueprint('messanger', __name__)


@bp.route('/messanger')
def messanger():

    db = get_db()

    # Select all (chats)
    # where (chat.user_1 == user_id or chat.user_2 == user_id)
    # sorted by (select message from messages where message.id == chat.last_message_id).sent_data
    # so chat with newest last message
    
    chat_rows = db.execute(
        """
        SELECT chats.*, COALESCE(messages.send_time, '1970-01-01 00:00:00') AS last_send_time
        FROM chats
        LEFT JOIN messages ON messages.id = chats.last_message_id
        WHERE chats.user_1 = ? OR chats.user_2 = ?
        ORDER BY last_send_time DESC;

        """, (session['user_id'], session['user_id'])
    ).fetchall()

    chats = []

    for chat_row in chat_rows:



        if chat_row['last_message_id'] is None:
            last_message = ""
        else:
            last_message = db.execute("SELECT * FROM messages WHERE id = ?;",
                                   (chat_row['last_message_id'])).fetchone()


        

        other_chat_user_id = chat_row['user_1'] if chat_row['user_1'] != session['user_id'] else chat_row['user_2']
        
        print(other_chat_user_id, type(other_chat_user_id))

        other_chat_user = db.execute("SELECT * FROM users WHERE id = ?;  ", (other_chat_user_id, )).fetchone()

        other_chat_user_last_name = ' ' + other_chat_user['last_name'] if other_chat_user['last_name'] else ''

        chats.append({
            'id': chat_row['id'],
            'last_message': last_message,
            'chat_name': other_chat_user['first_name'] + other_chat_user_last_name,
        })

    return render_template("messanger.html", chats=chats, logout_url=url_for('auth.logout', _external=True))
