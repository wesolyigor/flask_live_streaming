from flask import Blueprint, session, url_for, render_template
from flask_socketio import leave_room, emit, join_room
from werkzeug.utils import redirect

from app import socketio
from app.forms import UserForm, CommentatorForm

wslivestream = Blueprint('wslivestream', __name__, url_prefix='/livestream')


@wslivestream.route('/', methods=["GET", "POST"])
def livestream():
    name = session.get('name', '')
    room = session.get('room', '')

    if not name or not room:
        return redirect(url_for('main.home'))

    return render_template('livestream.html')


@socketio.on('joined', namespace='/livestream')
def joined(message):
    room = session.get('room')
    join_room(room)
    # emit('status', {'msg': f'{session.get("name")} dołączył do pokoju.'}, room=room)


@socketio.on('left', namespace='/livestream')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': f'{session.get("name")} opuścił pokój.'}, room=room)
