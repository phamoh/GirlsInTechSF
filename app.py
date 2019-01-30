from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Please create an endpoint with your name as the URL"

@app.route('names/olivia')
def olivia()
    return "I'm Olivia"

@app.route('/gitbranchexample')
def branch_example():
	return "This was created on a git branch"

