from flask import Flask

app = Flask(__name__)

#Static route
@app.route('/')
def hello_world():
    return 'Hello World!'

#Dynamic route
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'