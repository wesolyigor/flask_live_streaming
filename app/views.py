from flask import Blueprint, render_template, url_for, session
from werkzeug.utils import redirect

# from app.forms import UserForm, CommentatorForm
from app.forms import UserForm, CommentatorForm

bp_main = Blueprint('main', __name__, url_prefix='/')


@bp_main.route('/', methods=["GET", "POST"])
def home():
    form_user = UserForm()
    form_commentator = CommentatorForm()

    if form_user.validate_on_submit():
        session['room'] = form_user.room.data
        session['name'] = form_user.name.data
        return redirect(url_for('wslivestream.livestream'))

    if form_commentator.validate_on_submit():
        session['room_admin'] = form_commentator.room_admin.data
        return redirect(url_for('wscommentator.commentator'))

    return render_template('home.html', form_user=form_user, form_commentator=form_commentator)

