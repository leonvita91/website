
from flask import Flask, render_template, redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from content import LoginForm


#Init the Web
app = Flask (__name__)

app.config['SECRET_KEY'] = '018be4ee04cd65064e1443ce27349eda2c2d637f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(60),nullable=False)
    Posts = db.relationship('Post',backref='author',lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
    

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(500),nullable=False)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)


    def __repr__(slef):
        return f"Post('{self.title}')"




@app.route("/")
def home():
    return render_template("home.html")

#partner
@app.route("/associate")
def team():
    return render_template("associate.html")


#About_us
@app.route("/about_us")
def about():
    return render_template("about_us.html")



#loginPage
@app.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    return render_template("login.html",title='Login', form=form)




#End Init the Web
if __name__ == "__main__":
    app.run(debug=True)
