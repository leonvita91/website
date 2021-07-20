
from flask import Flask, render_template, redirect, url_for, request,flash
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from content import LoginForm,PostForm
from flask_login import LoginManager
from flask_login import login_user,logout_user,current_user,login_required
from flask_login import UserMixin
from flask_bcrypt import Bcrypt



#Init the Web
app = Flask (__name__)

app.config['SECRET_KEY'] = '018be4ee04cd65064e1443ce27349eda2c2d637f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
#End Init



class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(60),nullable=False)
    Posts = db.relationship('Post',backref='author',lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    first_post = Post.query.get(1)
    second_post = Post.query.get(2)
    third_post = Post.query.get(3)
    return render_template('home.html',first_post=first_post, second_post=second_post,
            third_post=third_post )


#partner
@app.route("/associate")
def team():
    return render_template("associate.html")


#About_us
@app.route("/about_us")
def about():
    return render_template("about_us.html")



#register
#@app.route("/sign_up",methods=['POST','GET'])
#def sign_up():
#    form = SignupForm()
#    if form.validate_on_submit():
#        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#        user = User(username=form.username.data, email=form.email.data,password=hashed_password)
#        db.session.add(user)
#        db.session.commit()        
#    return render_template("sign_up.html",form=form)



#loginPage
@app.route("/login",methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and  bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Welcome Admin!")
            return redirect(url_for('admin'))
        else:
            flash('Login in Unsuccessful,please try again!')
    return render_template("login.html", form=form)


#LogoutPage
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


#AdminPage
@app.route("/admin")
@login_required
def admin():
      return render_template("admin.html")


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!')
        return redirect(url_for('home'))
    return render_template('new_post.html', title='New Post',
                           form=form, legend='New Post')

@app.route("/update_posts")
@login_required
def update_post():
    return render_template('update_post.html', legend='Update Posts')



@app.route("/post/update1", methods=['GET', 'POST'])
@login_required
def update_post_1():
    post_id = 1
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('home'))
    return render_template('update_post_1.html', title='Update Post',
                           form=form, legend='Update Post')

@app.route("/post/update2", methods=['GET', 'POST'])
@login_required
def update_post_2():
    post_id = 2
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('home'))
    return render_template('update_post_2.html', title='Update Post',
                           form=form, legend='Update Post')

@app.route("/post/update3", methods=['GET', 'POST'])
@login_required
def update_post_3():
    post_id = 3
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('home'))
    return render_template('update_post_3.html', title='Update Post',
                           form=form, legend='Update Post')



#End Init the Web
if __name__ == "__main__":
    app.run(debug=True)
