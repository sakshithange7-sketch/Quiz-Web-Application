from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import TextQuestionForm, MCQForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ======================
# Database Model
# ======================
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    selected_answer = db.Column(db.String(50))
    is_correct = db.Column(db.Boolean)


# ======================
# Home
# ======================
@app.route('/')
def home():
    return "Quiz Running 🚀"


# ======================
# TEXT QUESTION
# ======================
@app.route('/text', methods=['GET', 'POST'])
def text_question():
    form = TextQuestionForm()
    result = None

    if form.validate_on_submit():
        answer = form.question.data

        new_result = Result(
            selected_answer=answer,
            is_correct=True
        )

        db.session.add(new_result)
        db.session.commit()

        result = f"You answered: {answer}"

    return render_template('text.html', form=form, result=result)


# ======================
# MCQ QUESTION
# ======================
@app.route('/mcq', methods=['GET', 'POST'])
def mcq_question():
    form = MCQForm()
    result = None

    if form.validate_on_submit():
        selected = form.answer.data
        correct = (selected == 'A')

        new_result = Result(
            selected_answer=selected,
            is_correct=correct
        )

        db.session.add(new_result)
        db.session.commit()

        result = f"You selected: {selected} | {'Correct' if correct else 'Wrong'}"

    return render_template('mcq.html', form=form, result=result)


# ======================
# RESULTS PAGE
# ======================
@app.route('/results')
def results():
    all_results = Result.query.all()
    return render_template('results.html', results=all_results)


# ======================
# RUN APP
# ======================
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)