from database import db


class Question(db.Model):
    question_id = db.Column("question_id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(600))
    posted_date = db.Column("posted_date", db.String(50))
    # num_likes = db.Column("title", db.Integer)
    # image = db.Column("image", db.Text)
    # category = db.Column("category", db.Text)
    # view_count = db.Column("view_count", db.Integer)

    def __init__(self, title, text, posted_date):
        self.title = title
        self.text = text
        self.posted_date = posted_date
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
# class Account(db.Model):
#     account_id = db.Column("account_id", db.Integer, primary_key=True)
#     account_type = db.Column("account_type", db.String(50))
#     last_name = db.Column("last_name", db.String(50))
#     first_name = db.Column("first_name", db.String(50))
#     email = db.Column("email", db.String(50))
#     phone_number = db.Column("phone_number", db.Integer)
#     username = db.Column("username", db.String(50))
#     profile_picture = db.Column("profile_picture", db.Blob)
#
#     def __init__(self, account_type, last_name, first_name, email, phone_number, username, profile_picture):
#         self.account_type = account_type
#         self.last_name = last_name
#         self.first_name = first_name
#         self.email = email
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



