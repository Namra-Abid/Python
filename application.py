from flask import Flask, render_template,url_for ,redirect,flash
from form import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='040976f416b05cf8aaf11939647f938c'
posts=[
     { 'author':'Namra',
        'title':'life',
        'content':'life is not bed of roses',
        'date_posted':'6 march 2020'
        },
        { 'author':'Raby',
           'title':'life',
           'content':'life is not bed of roses',
           'date_posted':'6 march 2020'
           }

]
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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
@app.route("/home")
def home():
    return render_template("index.html",posts=posts)
@app.route("/")
def index():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("title.html",title='About')
if '__name__'=='__main__':
    app.run(debug=True)
