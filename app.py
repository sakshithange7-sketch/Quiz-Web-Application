from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import TextQuestionForm, MCQForm

app = Flask(__name__)

# Config
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
    return "Quiz App Running 🚀"

# ======================
# TEXT QUESTION
# ======================
@app.route('/text', methods=['GET', 'POST'])
def text_question():

    form = TextQuestionForm()

    if form.validate_on_submit():

        answer = form.question.data

        new_result = Result(
            selected_answer=answer,
            is_correct=True
        )

        db.session.add(new_result)
        db.session.commit()

        message = f"Your Answer: {answer} (Recorded Successfully)"

        return render_template('confirmation.html', message=message)

    return render_template('text.html', form=form)

# ======================
# MCQ QUESTION
# ======================
@app.route('/mcq', methods=['GET', 'POST'])
def mcq_question():

    form = MCQForm()

    if form.validate_on_submit():

        selected = form.answer.data
        correct = (selected == 'A')

        new_result = Result(
            selected_answer=selected,
            is_correct=correct
        )

        db.session.add(new_result)
        db.session.commit()

        score = 1 if correct else 0

        message = f"Answer: {selected} | {'Correct' if correct else 'Wrong'} | Score: {score}/1"

        return render_template('confirmation.html', message=message)

    return render_template('mcq.html', form=form)
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