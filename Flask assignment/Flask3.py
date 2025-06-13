#3. Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask
app=Flask(__name__)
@app.route("/<name>")
def hello(name):
    return "Hello, there. My name is "+ name

if __name__=="__main__":
    app.run(debug=True)