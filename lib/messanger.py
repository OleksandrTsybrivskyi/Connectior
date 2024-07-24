from flask import Blueprint
from threading import Lock
from flask import Flask, render_template, session, url_for, redirect, request
from flask_socketio import SocketIO, emit, join_room, leave_room,rooms
from app import socketio
from datetime import datetime

from lib.db import get_db

bp = Blueprint('messanger', __name__)


@bp.route('/messanger', methods=('GET', 'POST'))
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

    if request.method == "POST":
        print("POST method")

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
    

    for chat_row in chat_rows:
        join_room(chat_row['id'])
        

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


    emit('chat_open_responce', response)


@socketio.on('send_message')
def send_message(data):
    '''
    Send message into the chat
    '''


    db = get_db()

    opened_chat_id = data["id"]
    sent_message = data["message"]

    db.execute("INSERT INTO messages(sender_id, chat_id, body) VALUES (?, ?, ?)", 
            (session["user_id"], opened_chat_id, sent_message,),)
    db.commit()
    last_message_id = db.execute("SELECT * FROM messages WHERE sender_id = ? ORDER BY send_time DESC",
            (session["user_id"],)).fetchone()["id"]
    print(last_message_id)
    db.execute("UPDATE chats SET last_message_id = ? WHERE id = ?", 
            (last_message_id, opened_chat_id))
    db.commit()
 
    emit('receive_message', to=opened_chat_id)
    print(opened_chat_id)

    # data = {"chat_id" : data["id"]}
    # open_chat(data=data)


@socketio.on('search_users')
def search_users(data):
    '''
    Search user
    '''

    db = get_db()

    search_prompt = data["search_prompt"]

    if "@" in search_prompt:
        results = db.execute("SELECT * FROM users WHERE nickname LIKE ?",
               ("%"+search_prompt+"%",)).fetchall()
    else:
        results = set()
        search_prompt_mass = search_prompt.split()
        for search_prompt_mass_element in search_prompt_mass:
            results_partial = db.execute("SELECT * FROM users WHERE first_name LIKE ?",
                ("%"+search_prompt_mass_element+"%",)).fetchall()
            for results_partial_element in results_partial:
                results.add(results_partial_element)
        for search_prompt_mass_element in search_prompt_mass:
            results_partial = db.execute("SELECT * FROM users WHERE last_name LIKE ?",
                ("%"+search_prompt_mass_element+"%",)).fetchall()
            for results_partial_element in results_partial:
                results.add(results_partial_element)
        results = list(results)
    
    return results
    
