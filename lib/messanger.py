from flask import Blueprint
from threading import Lock
from flask import Flask, render_template, session, url_for, redirect, request
from flask_socketio import SocketIO, emit
from app import socketio
from datetime import datetime

from lib.db import get_db

bp = Blueprint('messanger', __name__)


@bp.route('/messanger', methods=('GET', 'POST'))
def messanger():
    if session.get('user_id') is None:
        return redirect(url_for('auth.login'))

    db = get_db()
    if request.method == "POST":
        sent_message = request.form["sent_message"]
        oppenned_chat_id = 5 #TODO oppened_chat_id must be an id of a current chat

        db.execute("INSERT INTO messages(sender_id, chat_id, body) VALUES (?, ?, ?)", 
                (session["user_id"], oppenned_chat_id, sent_message,),)
        db.commit()
        last_message_id = db.execute("SELECT * FROM messages WHERE sender_id = ? ORDER BY send_time DESC",
                (session["user_id"],)).fetchone()["id"]
        db.execute("UPDATE chats SET last_message_id = ? WHERE id = ?", 
                (last_message_id, oppenned_chat_id))
        db.commit()

    
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
                                   (chat_row['last_message_id'],)).fetchone()['body']
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

@socketio.on('connect')
def connect():
    '''
    Send all users chat_id's to client
    '''

    db = get_db()

    chat_rows = db.execute(
        """
        SELECT * FROM chats
        WHERE user_1 = ? OR user_2 = ?
        """, (session['user_id'], session['user_id'],))
    
    chat_ids = []

    for chat_row in chat_rows:
        chat_ids.append(chat_row['id'])

    response = {
        "ids": chat_ids
    }

    emit('chat_ids', response)

@socketio.on('open_chat')
def open_chat(data):
    '''
    Recieve "chat_id" from client
    '''
    print('Received data:', data)

    db = get_db()
    
    message_rows = db.execute(
        """
        SELECT * FROM messages
        WHERE chat_id = ?
        ORDER BY send_time DESC
        LIMIT 50;
        """,
        (data['chat_id'],)
    ).fetchall()
    
    messages = []
    for message_row in message_rows:

        message_my = message_row['sender_id'] == session['user_id']

        send_time = datetime.strftime(message_row['send_time'], "%d %b  %H:%M")


        messages.append({
            'message_my': message_my,
            'viewed': message_row['viewed'],
            'body': message_row['body'],
            'send_time': send_time
        })
        
    response = {
        'messages': messages
    }

    print(response)

    emit('chat_open_responce', response)


# @bp.route('/post', methods=('GET', 'POST'))
# def post():
#     db = get_db()

#     sent_message = request.args.get('sent_message')
#     oppenned_chat_id = None

#     db.execute("INSERT INTO messages(sender_id, chat_id, body) VALUES (?, ?, ?)", 
#                (session["user_id"], oppenned_chat_id, sent_message,),)
#     db.commit()
#     last_message_id = db.execute("SELECT LAST_INSERT_ID()")
#     db.execute("UPDATE chats SET last_message_id = ? WHERE id = ?", 
#                (last_message_id, oppenned_chat_id))
#     db.commit()

#     redirect(url_for('messanger.messanger'))




