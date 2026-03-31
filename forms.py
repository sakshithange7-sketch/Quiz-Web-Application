from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

class TextQuestionForm(FlaskForm):
    question = StringField('Your Answer', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MCQForm(FlaskForm):
    answer = RadioField('Choose an option', choices=[
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')