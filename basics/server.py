from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "This is home pahe method"

@app.route('/hello')
def hello():
    return "print hello function called"



app.run()

