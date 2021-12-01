from database import db
import datetime


class Question(db.Model):
    question_id = db.Column("question_id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(600))
    posted_date = db.Column("posted_date", db.String(50))
    # creating a foreign key: referencing the id variable in the User class, so that is why it is lowercase u
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    replies = db.relationship("Reply", backref="question", cascade="all, delete-orphan", lazy=True)
    view_count = db.Column("view_count", db.Integer, default=0)
    num_likes = db.Column("Upvotes", db.Integer, db.ForeignKey("user.user_id"), db.ForeignKey("question.question_id"), default=0)
    # image = db.Column("image", db.Text)
    # category = db.Column("category", db.Text)

    def __init__(self, title, text, posted_date, user_id, view_count, num_likes):
        self.title = title
        self.text = text
        self.posted_date = posted_date
        self.user_id = user_id
        self.view_count = view_count
        self.num_likes = num_likes
        # self.image = image
        # self.category = category


# class Login(db.Model):
#     account_id = db.Column("account_id", db.Integer, primary_key=True)
#     password = db.Column("password", db.String(50))
#
#     def __init__(self, password):
#         self.password = password
#
#

class User(db.Model):
    user_id = db.Column("user_id", db.Integer, primary_key=True)
    #     account_type = db.Column("account_type", db.String(50))
    last_name = db.Column("last_name", db.String(50))
    first_name = db.Column("first_name", db.String(50))
    email = db.Column("email", db.String(50))
    password = db.Column(db.String(50), nullable=False)
    registered_on = db.Column("posted_date", db.String(50))
    replies = db.relationship("Reply", backref="user", lazy=True)
    num_of_posts = db.Column("num_of_posts", db.Integer, default=0)
    #     questions = db.relationship("Question", backref="user", lazy=True)
    #     phone_number = db.Column("phone_number", db.Integer)
    #     username = db.Column("username", db.String(50))
    #     profile_picture = db.Column("profile_picture", db.Blob)

    def __init__(self, first_name, last_name, email, password, registered_on, num_of_posts):
        #       self.account_type = account_type
        self.user_id = self.user_id
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.password = password
        self.registered_on = registered_on
        self.num_of_posts = num_of_posts
#         self.phone_number = phone_number
#         self.username = username
#         self.profile_picture = profile_picture


class Reply(db.Model):
    reply_id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.VARCHAR, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.question_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

    def __init__(self, content, question_id, user_id):
        self.date_posted = datetime.date.today()
        self.content = content
        self.question_id = question_id
        self.user_id = user_id

#
#
# class canPost(db.Model):
#     account_id = db.Column("account_id", db.Integer, primary_key=True)
#     question_id = db.Column("question_id", db.Integer)
#
#     def __init__(self, question_id):
#         self.question_id = question_id

