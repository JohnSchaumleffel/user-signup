from flask import Flask, request, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup-form.html')
 
@app.route("/", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome-page.html', username=username)

app.run()
