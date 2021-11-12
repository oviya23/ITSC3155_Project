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
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home/question/edit/delete/<question_id>', methods=['POST'])
def delete_note(question_id):
    # retrieve question from database
    my_question = db.session.query(Question).filter_by(id=question_id).one()
    db.session.delete(my_question)
    db.session.commit()

    return redirect(url_for('home'))

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.
