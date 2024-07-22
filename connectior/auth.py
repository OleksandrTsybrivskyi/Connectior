from connectior.lib.verification import *
from connectior.lib.email_actions import *

from datetime import datetime, timezone

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from connectior.db import get_db, sql_time_to_python_time

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        nickname = request.form['nickname']
        
        db = get_db()

        if not verify_email(email):
            error = 'Invalid email address.'
        elif not verify_password(password):
            error = 'Invalid password.'
        elif not verify_first_name(first_name):
            error = 'Invalid first name.'
        elif not verify_last_name(last_name):
            error = 'Invalid last name.'
        elif not verify_nickname(nickname):
            error = 'Invalid nickname.'
        
        if error is None:
            check_if_email_exists = db.execute(
                    'SELECT 1 FROM users WHERE email = ?', (email,)
                ).fetchone()
            check_if_nickname_exists = db.execute(
                    'SELECT 1 FROM users WHERE nickname = ?', (nickname,)
                ).fetchone()

            if check_if_email_exists and check_if_nickname_exists:
                error = f"User {email} is already registered.\nUser @{nickname} is already registered."
            elif check_if_email_exists:
                error = f"User {email} is already registered."
            elif check_if_nickname_exists:
                error = f"User {nickname} is already registered."
            else:
                activation_code = send_email_activation_letter(email)
                sent_time = int(time.time())
                db.execute(
                    "INSERT INTO unactivated_users (email, password, first_name, last_name, nickname, activation_code, sent_time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (email, generate_password_hash(password), first_name, last_name, nickname, activation_code, sent_time,),
                )
                db.commit()
                return redirect(url_for('auth.check_inbox'))


    return render_template('register.html', error=error)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    if request.method == 'POST':
        email_or_nickname = request.form['email_or_nickname']
        password = request.form['password']
        db = get_db()
        user = None

        if not verify_email(email_or_nickname):
            error = 'Incorrect email.'
        elif not verify_password(password):
            error = 'Incorrect password.'
        else:
            if '@' in email_or_nickname:
                user = db.execute(
                    'SELECT * FROM users WHERE email = ?', (email_or_nickname,)
                ).fetchone()
            else:
                user = db.execute(
                    'SELECT * FROM users WHERE nickname = ?', (email_or_nickname,)
                ).fetchone()

        if user is None:
            error = 'Incorrect email or nickname.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('messanger'))


    return render_template('login.html')


@bp.route('/activate/activation_code=<string:activation_code>', methods=('GET', 'POST'))
def activate(activation_code):

    db = get_db()
    user = db.execute(
        'SELECT * FROM unactivated_users WHERE activation_code = ? ORDER BY sent_time DESC', (activation_code,)
    ).fetchone()

    if user != None:
        current_time = time.time()
        if current_time - user["sent_time"] <= 600:
            try:
                db.execute(
                    "INSERT INTO users (email, password, first_name, last_name, nickname) VALUES (?, ?, ?, ?, ?)",
                    (user["email"], user["password"], user["first_name"], user["last_name"], user["nickname"],),
                )
                db.commit()
            except:
                flash("Activation code is already used")
                return redirect(url_for("auth.register"))
            else:
                flash("Your account has been activated. Please, login to your account.")
                return redirect(url_for("auth.login"))
        else:
            flash("Activation code has been expired. Complete registration again.")
            return redirect(url_for("auth.register"))
    
    flash("Wrong activation code")
    return redirect(url_for("auth.register"))
        


@bp.route('/check_inbox', methods=('GET', 'POST'))
def check_inbox():
    return render_template("check_inbox.html")
