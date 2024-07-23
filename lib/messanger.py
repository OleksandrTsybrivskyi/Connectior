from flask import Blueprint
from threading import Lock
from flask import Flask, render_template, session, url_for, redirect
from flask_socketio import SocketIO, emit
from app import socketio

from lib.db import get_db

bp = Blueprint('messanger', __name__)


@bp.route('/messanger')
def messanger():

    if session.get('user_id') is None:
        return redirect(url_for('auth.login'))

    db = get_db()
    
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

        # Handle last message
        if chat_row['last_message_id'] is None:
            last_message = ""
        else:
            last_message = db.execute("SELECT * FROM messages WHERE id = ?;",
                                   (chat_row['last_message_id'])).fetchone()['body']
            if len(last_message) > 20:
                last_message = last_message[:17] + '...'


        
        # Handle chat name
        other_chat_user_id = chat_row['user_1'] if chat_row['user_1'] != session['user_id'] else chat_row['user_2']
        other_chat_user = db.execute("SELECT * FROM users WHERE id = ?;  ", (other_chat_user_id, )).fetchone()
        other_chat_user_last_name = ' ' + other_chat_user['last_name'] if other_chat_user['last_name'] else ''
        chat_name = other_chat_user['first_name'] + other_chat_user_last_name
        if len(chat_name) > 15:
            chat_name = chat_name[:12] + '...'


        chats.append({
            'id': chat_row['id'],
            'last_message': last_message,
            'chat_name': chat_name,
        })

    current_user = db.execute("SELECT * FROM users WHERE id = ?;", (session['user_id'], )).fetchone()
    current_user_info = {
        'id': current_user['id'],
        'first_name': current_user['first_name'],
        'last_name': current_user['last_name'],
        'nickname': current_user['nickname'],
        'email': current_user['email'],
    }

    logout_url = url_for('auth.logout', _external=True)

    return render_template("messanger.html",
                           chats=chats,
                           current_user_info=current_user_info,
                           logout_url=logout_url)

@socketio.on('open_chat')
def handle_custom_event(data):
    print('Received data:', data)

    db = get_db()
    
    message_rows = db.execute(
        "SELECT * FROM messages WHERE chat_id = ?;",
        (data['chat_id'],)
    ).fetchone()
    
    messages = []
    for message_row in message_rows:

        message_my = message_row['sender_id'] == session['user_id']

        messages.append({
            'message_my': message_my,
            'viewed': message_row['viewed'],
            'body': message_row['body'],
            'send_time': message_row['send_time']
        })

    response_data = {
        'response': messages
    }
    
    # Send a response back to the client
    emit('chat_open_responce', response_data)