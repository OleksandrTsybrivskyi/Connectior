import functools
from connectior.lib.verification import *

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from connectior.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

import os
from email.message import EmailMessage
import ssl
import smtplib

import hashlib
import random

import time

def create_activation_code():
    """Hashes a password using the SHA-256 algorithm."""
    hash_object = hashlib.sha256()
    random_number = str(random.randint(0, 999999999)) + "dev" #dev must be replaced with random string
    hash_object.update(random_number.encode('utf-8'))
    return hash_object.hexdigest()


def email_verif(email_receiver):
    email_sender = "kodova.bryhada@gmail.com"
    # email_password = os.environ.get("EMAIL_PASSWORD")
    email_password = "djfb xumm nfcv mpxl"
    email_receiver = "tsybrivsky@gmail.com"

    activation_code = create_activation_code()

    subject = "Account activation"
    body = f"""
    To activate your Connectior account follow this link:
    http://127.0.0.1:5000/auth/activate/activation_code={activation_code}
    """

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return activation_code


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
            try:
                activation_code = email_verif(email)
                sent_time = int(time.time())
                db.execute(
                    "INSERT INTO unactivated_users (email, password, first_name, last_name, nickname, activation_code, sent_time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (email, generate_password_hash(password), first_name, last_name, nickname, activation_code, sent_time,),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {email} is already registered."
            else:
                return redirect(url_for("auth.check_inbox"))


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
            return redirect(url_for('index'))


<<<<<<< HEAD
    return render_template('login.html', error=error)
error = None
=======
    return render_template('auth/login.html')


@bp.route('/activate/activation_code=<string:activation_code>', methods=('GET', 'POST'))
def activate(activation_code):

    db = get_db()
    user = db.execute(
        'SELECT * FROM unactivated_users WHERE activation_code = ? ORDER BY sent_time DESC', (activation_code,)
    ).fetchone()
    if not user:
        current_time = time.time()
        if current_time - user.sent_time <= 300:
            db.execute(
                "INSERT INTO users (email, password, first_name, last_name, nickname) VALUES (?, ?, ?, ?, ?)",
                (user.email, user.password, user.first_name, user.last_name, user.nickname,),
            )
            db.commit()
            flash("Yor account has been activated. Please, login to your account")
            return redirect(url_for("auth.login"))
        else:
            flash("Activation code has been expired. Complete registration again")
            return redirect(url_for("auth.register"))
    else:
        flash("Wrong activation code")
        return redirect(url_for("auth.register"))


@bp.route('/check_inbox', methods=('GET', 'POST'))
def check_inbox():
    return render_template("auth/check_inbox.html")
>>>>>>> 140fd855e0702f2bff51c25df404c3136830aba2
