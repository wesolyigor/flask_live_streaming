from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name = StringField(label='Your name:', validators=[DataRequired()])
    room = StringField(label='Room name:', validators=[DataRequired()])
    submit = SubmitField(label='LOGIN', validators=[DataRequired()])


class CommentatorForm(FlaskForm):
    room_admin = StringField(label='Room name:', validators=[DataRequired()])
    submit = SubmitField(label='CREATE', validators=[DataRequired()])
