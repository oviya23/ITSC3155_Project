from database import db
import datetime


class Question(db.Model):
    question_id = db.Column("question_id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(600))
    posted_date = db.Column("posted_date", db.String(50))
    # creating a foreign key: referencing the id variable in the User class, so that is why it is lowercase u
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

    # num_likes = db.Column("title", db.Integer)
    # image = db.Column("image", db.Text)
    # category = db.Column("category", db.Text)
    # view_count = db.Column("view_count", db.Integer)

    def __init__(self, title, text, posted_date, user_id):
        self.title = title
        self.text = text
        self.posted_date = posted_date
        self.user_id = user_id
        # self.num_likes = num_likes
        # self.image = image
        # self.category = category
        # self.view_count = view_count


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
    registered_on = db.Column(db.DateTime, nullable=False)

    #     questions = db.relationship("Question", backref="user", lazy=True)
    #     phone_number = db.Column("phone_number", db.Integer)
    #     username = db.Column("username", db.String(50))
    #     profile_picture = db.Column("profile_picture", db.Blob)
    #
    def __init__(self, first_name, last_name, email, password):
        #       self.account_type = account_type
        self.user_id = self.user_id
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.password = password
        self.registered_on = datetime.date.today()
#         self.phone_number = phone_number
#         self.username = username
#         self.profile_picture = profile_picture
#
#
# class canPost(db.Model):
#     account_id = db.Column("account_id", db.Integer, primary_key=True)
#     question_id = db.Column("question_id", db.Integer)
#
#     def __init__(self, question_id):
#         self.question_id = question_id
