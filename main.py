from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os
from flask_bootstrap import Bootstrap5

# Initializes Flask app and Bootstrap:
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Setting up environment variables before app initialization
app.config['SECRET_KEY'] = os.environ.get('MYSECRETKEY', 'a_default_secret')
email = os.environ.get('MYSECRETUSERNAME', 'default-secret-username')
password = os.environ.get('MYSECRETPASSWORD', 'default-secret-password')

class MyLoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()], render_kw={"size": "30"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4, max=30)], render_kw={"size": "30"})
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyLoginForm()
    if form.validate_on_submit():  # If a successful validation, then True
        if form.email.data == email and form.password.data == password:
            print(form.email.data)
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    else:
        # Form is not valid, print or log the errors
        print(form.errors)
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
