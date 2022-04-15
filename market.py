from flask import Flask, render_template

app = Flask(__name__)

#Two Routes in one!
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')