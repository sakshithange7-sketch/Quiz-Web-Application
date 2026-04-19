from flask import Flask, render_template
from forms import TextQuestionForm, MCQForm

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Home route
@app.route('/')
def home():
    return '''
    <h2>Welcome to Quiz App</h2>
    <a href="/text">Text Question</a><br><br>
    <a href="/mcq">MCQ Question</a>
    '''

# Text question route
@app.route('/text', methods=['GET', 'POST'])
def text_question():
    form = TextQuestionForm()
    if form.validate_on_submit():
        return f"You answered: {form.question.data}"
    return render_template('text.html', form=form)

# MCQ route
@app.route('/mcq', methods=['GET', 'POST'])
def mcq_question():
    form = MCQForm()
    if form.validate_on_submit():
        return f"You selected: {form.answer.data}"
    return render_template('mcq.html', form=form)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
    class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    selected_answer = db.Column(db.String(10))
    is_correct = db.Column(db.Boolean)