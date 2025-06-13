# 2. Build a Flask app with static HTML pages and navigate between them.
from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/next_page")
def next_page():
    return render_template("next_page.html")
if __name__=="__main__":
    app.run(debug=True)