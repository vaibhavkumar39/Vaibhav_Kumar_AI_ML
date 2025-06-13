#5. Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, request, render_template, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "vaibhav123"
@app.route("/")
def home():
    return render_template("login.html")
@app.route("/login", methods=["POST"])
def login():
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    session['city'] = request.form['city']
    return redirect(url_for("profile"))
@app.route("/profile")
def profile():
    if 'name' not in session:
        return redirect(url_for("home"))
    return f'''
        <h1>Your Data (From Session)</h1>
        Your name: {session['name']}<br><br>
        Your age: {session['age']}<br><br>
        Your city: {session['city']}<br><br>
        <a href="/logout">Logout</a>
    '''
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)