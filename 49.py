# *QUESTION 49* Make a fully functional web application using Flask and MongoDB. Signup, Signin page. And after successfully login, display a "Hello Geeks" message on the webpage.

from flask import Flask, request, redirect, url_for, render_template_string, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        mongo.db.users.insert_one({'username': username, 'password': password})
        return redirect(url_for('signin'))
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            Password: <input type="password" name="password">
            <input type="submit">
        </form>
    '''

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials'
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            Password: <input type="password" name="password">
            <input type="submit">
        </form>
    '''

@app.route('/home')
def home():
    if 'username' in session:
        return 'Hello Geeks!'
    return redirect(url_for('signin'))

if __name__ == "__main__":
    app.run(debug=True)
