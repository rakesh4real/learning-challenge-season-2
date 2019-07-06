# Only inport packages and modules necessary for this script code

from flask import render_template, url_for, flash, redirect
# Additional packages db and bcrypt imported
from myapp import app, db, bcrypt
# Note: myapp.forms, myapp.models
from myapp.forms import RegistrationForm, LoginForm
from myapp.models import User, Post


posts = [
    {
        'author': 'Sisira Mathews',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'July 2, 2019'
    },
    {
        'author': 'Alan Turing',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'July 1, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Connected the registration page to database
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)