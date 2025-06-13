#8. Implement user authentication and registration in a Flask app using Flask-Login.
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user

app = Flask(__name__)
app.secret_key = 'abc123'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

users = {}

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        return self.id


@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
@login_required
def home():
    return f"Hi welcome to the page,{current_user.username}"  


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users.values():
            if user.username == username and user.password == password:
                login_user(user)
                return redirect(url_for('home'))

        flash('Invalid username or password')
    return render_template('login_page.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users.values():
            if user.username == username:
                flash('Username already exists')
                return redirect(url_for('signup'))

        user_id = str(len(users) + 1)
        new_user = User(user_id, username, password)
        users[user_id] = new_user

        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)