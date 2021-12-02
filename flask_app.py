# imports
import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Question as Question
from models import User as User
from forms import RegisterForm, ReplyForm
from forms import LoginForm
import bcrypt
from flask import session
from models import Reply as Reply

app = Flask(__name__)  # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_qa_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SE3155'
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# Setup models
with app.app_context():
    db.create_all()  # run under the app context


@app.route('/')
@app.route('/home')
def index():
    # retrieve user from database
    # retrieve questions from database
    if session.get('user'):
        my_questions = db.session.query(Question).all()

        return render_template('home.html', post=my_questions, user=session['user'], userID=session['user_id'])
    else:
        return redirect(url_for('login'))


@app.route('/home/profile')
def get_profile():
    # retrieve user from database
    if session.get('user'):
        my_user = db.session.query(User).filter_by(user_id=session['user_id']).one()

        return render_template('profile.html', user=my_user)
    else:
        return redirect(url_for('login'))


@app.route('/home/<question_id>', methods=['GET', 'POST'])
def get_question(question_id):
    if session.get('user'):

        my_question = db.session.query(Question).filter_by(question_id=question_id).one()

        # increment view count everytime question page is accessed
        my_question.view_count += 1

        #if request.method == 'POST':
        #    my_question.num_likes += 1

        #my_question.num_likes += 1
        if request.method == 'POST':
            my_question.num_likes += 1

        # update question in database
        db.session.add(my_question)
        db.session.commit()

        # create a reply form object
        form = ReplyForm()

        return render_template('question.html', question=my_question, form=form, num_likes=my_question.num_likes)
    else:
        return redirect(url_for('login'))


def like_button(question_id):
    if session.get('user'):
        my_question = db.session.query(Question).filter_by(question_id=question_id).one()
        if request.method == 'GET':
            my_question.num_likes += 1

            db.session.add(my_question)
            db.session.commit()
            return render_template('question.html', question=my_question, num_likes=my_question.num_likes)
        return redirect(url_for('like_button'))


@app.route('/home/new', methods=['GET', 'POST'])
def new_post():
    if session.get('user'):
        if request.method == 'POST':
            title = request.form['title']
            text = request.form['postText']

            from datetime import date
            today = date.today()

            today = today.strftime("%m-%d-%Y")

            new_record = Question(title, text, today, session['user_id'], 0, 0)
            db.session.add(new_record)
            db.session.commit()

            curr_user = db.session.query(User).filter_by(user_id=session['user_id']).one()
            curr_user.num_of_posts += 1
            db.session.add(curr_user)
            db.session.commit()

            return redirect(url_for('index'))
        else:
            return render_template('new_post.html', user=session['user'])
    else:
        return redirect(url_for('login'))


@app.route('/home/edit/<question_id>', methods=['GET', 'POST'])
def edit_post(question_id):
    if session.get('user'):
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

            return render_template('new_post.html', question=my_question, user=session['user'])
    else:
        return redirect(url_for('login'))


@app.route('/home/delete/<question_id>', methods=['POST'])
def delete_post(question_id):
    if session.get('user'):
        # retrieve question from database
        my_question = db.session.query(Question).filter_by(question_id=question_id).one()

        db.session.delete(my_question)
        db.session.commit()

        curr_user = db.session.query(User).filter_by(user_id=session['user_id']).one()
        curr_user.num_of_posts -= 1
        db.session.add(curr_user)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        # salt and hash password
        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        # get entered user data
        first_name = request.form['firstname']
        last_name = request.form['lastname']

        from datetime import date
        today = date.today()

        today = today.strftime("%m-%d-%Y")

        # create user model
        new_user = User(first_name, last_name, request.form['email'], h_password, today, 0)
        # add user to database and commit
        db.session.add(new_user)
        db.session.commit()
        # save the user's name to the session
        session['user'] = first_name
        session['user_id'] = new_user.user_id  # access id value from user model of this newly added user
        # show user dashboard view
        return redirect(url_for('index'))

    # something went wrong - display register view
    return render_template('registration.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    # validate_on_submit only validates using POST
    if login_form.validate_on_submit():
        # we know user exists. We can use one()
        the_user = db.session.query(User).filter_by(email=request.form['email']).one()
        # user exists check password entered matches stored password
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            # password match add user info to session
            session['user'] = the_user.first_name
            session['user_id'] = the_user.user_id
            # render view
            return redirect(url_for('index'))

        # password check failed
        # set error message to alert user
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        # form did not validate or GET request
        return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    # check if a user is saved in session
    if session.get('user'):
        session.clear()

    return redirect(url_for('index'))


@app.route('/home/<question_id>/reply', methods=['POST'])
def new_reply(question_id):
    if session.get('user'):
        reply_form = ReplyForm()
        # validate_on_submit only validates using POST
        if reply_form.validate_on_submit():
            # get comment data
            reply_text = request.form['reply']
            new_record = Reply(reply_text, int(question_id), session['user_id'])
            db.session.add(new_record)
            db.session.commit()

        return redirect(url_for('get_question', question_id=question_id))

    else:
        return redirect(url_for('login'))


@app.route('/home/<question_id>/like/<action>')
def like_action(question_id, action):
    post = db.session.query(Question).filter_by(question_id=question_id).first_or_404()
    curr_user = db.session.query(User).filter_by(user_id=session['user_id']).one()
    if action == 'like':
        curr_user.like_post(post)
        db.session.commit()
    return redirect(url_for('get_question', question_id=question_id))


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.
