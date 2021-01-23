from flask import Blueprint, session, url_for, render_template
from flask_socketio import leave_room, emit, join_room, send
from werkzeug.utils import redirect

from app import socketio
from app.forms import CommentatorForm

wscommentator = Blueprint('wscommentator', __name__, url_prefix='/commentator')


@wscommentator.route('/', methods=["GET", "POST"])
def commentator():
    name = 'Admin'
    room = session.get('room_admin', '')
    if not name or not room:
        return redirect(url_for('main.home'))
    return render_template('commentator.html', room=room)


@socketio.on('message', namespace='/comentator')
def handle_message(message):
    print(message["msg"])
    room = session.get('room')
    emit('message', message["msg"], room=room, namespace='/livestream', broadcast=True)


# @socketio.on('joined', namespace='/livestream')
# def joined(message):
#     room = session.get('room')
#     join_room(room)
# emit('status', {'msg': f'{session.get("name")} dołączył do pokoju.'}, room=room)


@socketio.on('joined', namespace='/commentator')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('message', {'msg': f'{session.get("name")} dołączył do pokoju.'}, room=room, broadcast=True,
         namespace='/livestream')


@socketio.on('left', namespace='/commentator')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': f'{session.get("name")} opuścił pokój.'}, room=room)
