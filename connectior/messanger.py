from flask import Blueprint, render_template, session, url_for
from connectior.db import get_db



bp = Blueprint('messanger', __name__)


@bp.route('/messanger') 
def messanger():
    db = get_db()

    # chats = db.execute(
    #     """
    #     SELECT chat.* messages.send_time
    #     FROM chats
    #     WHERE user_1 = ? OR user_2 = ?
    #     ORDER BY (SELECT * FROM messages WHERE last_message_id)
    #     """, (session['user_id'], session['user_id'])
    # ).fetchall()

    chats = db.execute(
        """
        SELECT chats.* messages.send_time
        FROM chats
        WHERE user_1 = ? OR user_2 = ?
        ORDER BY (SELECT * FROM messages WHERE last_message_id) DESC
        """, (session['user_id'], session['user_id'])
    ).fetchall()

    print(chats)

    return render_template("messanger.html", chats=chats, logout_url=url_for('auth.logout'))