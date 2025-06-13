#11. Create a real-time chat application using Flask-SocketIO.
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def home():
    return "<h1>Add user1 and user2 in url to use chatapp</h1>"

@app.route('/user1')
def user1():
    return render_template('user1.html')

@app.route('/user2')
def user2():
    return render_template('user2.html')

@socketio.on('message')
def handle_message(msg):
    print('Message:', msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)