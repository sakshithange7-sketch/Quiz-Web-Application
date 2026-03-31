from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from forms import TextQuestionForm, MCQForm

app = Flask(__name__)

# Secret key for forms
app.config['SECRET_KEY'] = 'secret123'

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'

db = SQLAlchemy(app)

# ---------------- MODELS ----------------

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    is_correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return "Quiz Backend Running"

@app.route('/text', methods=['GET', 'POST'])
def text_question():
    form = TextQuestionForm()
    if form.validate_on_submit():
        return f"You answered: {form.question.data}"
    return str(form.question.label) + str(form.question) + str(form.submit)

@app.route('/mcq', methods=['GET', 'POST'])
def mcq_question():
    form = MCQForm()
    if form.validate_on_submit():
        return f"You selected: {form.answer.data}"
    return str(form.answer.label) + str(form.answer) + str(form.submit)

# ---------------- RUN ----------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)