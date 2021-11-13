# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
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
    return render_template('home.html')


@app.route('/home/question/edit/<question_id>', methods=['GET', 'POST'])
def edit_post(question_id):
    if request.method == 'POST':
        # get title data
        title = request.form['title']

        # get post text
        text = request.form['postText']
        post = db.session.query(Question).filter_by(id=question_id).one()

        # update question title and text
        post.title = title
        post.text = text

        # update question in database
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('get_question'))
    else:
        # GET request - show new question form to edit the question
        # retrieve user from database
        # Fix this line -----
        # a_user = db.session.query(Account).filter_by(username="test").one()

        # retrieve question from database
        my_question = db.session.query(Question).filter_by(id=question_id).one()

        return render_template('edit.html', post=my_question)


app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.
