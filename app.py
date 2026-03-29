from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'

db = SQLAlchemy(app)

# Quiz Model
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

# Question Model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))

# Choice Model
class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    is_correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

@app.route('/')
def home():
    return "Quiz Backend Running"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)