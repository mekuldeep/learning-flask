from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def print_hello():
    return "This is basic flask application..!"
    
app.run(debug=True)