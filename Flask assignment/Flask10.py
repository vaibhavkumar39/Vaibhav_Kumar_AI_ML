#10. Design a Flask app with proper error handling for 404 and 500 errors.
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.errorhandler(404)
def page_not_found(e):
    return {"error": "The requested URL was not found."}, 404

@app.errorhandler(500)
def internal_error(e):
    return {"error": "Something went wrong on the server. Try again later."}, 500

if __name__ == '__main__':
    app.run(debug=True)
