from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# Used to generate secured cookies to avoid vulnerabilities
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Sisra Mathews',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'July 2, 2019'
    },
    {
        'author': 'Alan Turing',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'July 1, 2018'
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
    # Create RegistrationForm object from class in forms.py
    form = RegistrationForm()
    # Validate form then render register page
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # Create LoginForm object from forms.py
    form = LoginForm()
    # validate entries in the form
    if form.validate_on_submit():
        # Creating dummy data to check the login functions
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
