import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from connectior.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        nickname = request.form['nickname']
        
        db = get_db()
        error = None

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif not first_name:
            error = 'First name is required.'
        elif not nickname:
            error = 'Nickname is required.'
        

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (email, password, first_name, last_name, nickname) VALUES (?, ?, ?, ?, ?)",
                    (email, generate_password_hash(password), first_name, last_name, nickname),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {email} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')