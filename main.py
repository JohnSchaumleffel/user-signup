from flask import Flask, request,redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup-form.html')

@app.route("/", methods=['POST'])
def validate_inputs():

    username = ''
    email = ''
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

    if username == '':
        username_error = "Please enter a valid username."
        username = ''

    for char in username:
        if char.isspace():
            username_error = "Username cannot contain spaces."
            username = ''
        else:
            if (len(username) < 3) or (len(username) > 20):
                username_error = 'Username must be between 3-20 characters.'
                username = ''

        if not username:
            username_error = "Please enter a valid username."
            username = ''

    if password == '':
        password_error = "Please enter a valid password."

    for char in password:
        if char.isspace():
            password_error = "Password cannot contain spaces."
            password = ''
        elif (len(password) < 3) or (len(password) > 20):
            password_error = "Password must be between 3-20 characters."
            password = ''
        elif not len(password):
            password_error = "Please enter a valid password."
            password = ''

    if verify == '':
        verify_error = "Please retype your password."
    
    if password != verify:
        verify_error = "The passwords do not match."
        verify = ''

    if email == '':
        email_error = ""
    elif "@" not in email:
        email_error = "This is not a valid email."
        email = ''
    elif "." not in  email:
        email_error = "This is not a valid email."
        email = ''
    elif " " in email:
        email_error = "This is not a valid email."
        email = ''
    elif (len(email) < 3) or (len(email) > 20):
        email_error = "This not a valid email."
        email = ''
    
    if (not username_error) and (not password_error) and (not verify_error) and (not email_error):
        username = username
        return render_template('welcome-page.html', username = username)
    else: 
        return render_template('signup-form.html', username_error=username_error, username=username, password_error = password_error, email = email, verify_error = verify_error, email_error = email_error)
        

app.run()
