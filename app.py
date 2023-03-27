from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome To My AAG Motors ... Thank you for coming we are located on akala express way'
