from flask import Flask, render_template
from .. import app
from .models import User

@app.route('/user/signup/', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/user/test/', methods=['GET'])
def testlogin():
    return render_template('tickets.html', username='test')