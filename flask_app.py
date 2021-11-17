# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Question as Question

app = Flask(__name__)     # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_qa_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# Setup models
with app.app_context():
    db.create_all()   # run under the app context


@app.route('/')
@app.route('/home')
def index():
    # retrieve user from database
    # retrieve questions from database
    my_questions = db.session.query(Question).all()

    return render_template('home.html', post=my_questions)


@app.route('/home/<question_id>')
def get_question(question_id):
    my_question = db.session.query(Question).filter_by(question_id=question_id).one()
    return render_template('question.html', question=my_question)


@app.route('/home/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['postText']

        from datetime import date
        today = date.today()

        today = today.strftime("%m-%d-%Y")

        new_record = Question(title, text, today)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('new_post.html')


@app.route('/home/edit/<question_id>', methods=['GET', 'POST'])
def edit_post(question_id):
    if request.method == 'POST':
        # get title data
        title = request.form['title']

        # get post text
        text = request.form['postText']
        question = db.session.query(Question).filter_by(question_id=question_id).one()

        # update question title and text
        question.title = title
        question.text = text

        # update question in database
        db.session.add(question)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        # GET request - show new question form to edit the question
        # retrieve user from database
        # Fix this line -----
        # a_user = db.session.query(Account).filter_by(username="test").one()

        # retrieve question from database
        my_question = db.session.query(Question).filter_by(question_id=question_id).one()

        return render_template('new_post.html', question=my_question)


@app.route('/home/delete/<question_id>', methods=['POST'])
def delete_post(question_id):
    # retrieve question from database
    my_question = db.session.query(Question).filter_by(question_id=question_id).one()
    db.session.delete(my_question)
    db.session.commit()

    return redirect(url_for('index'))


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.
