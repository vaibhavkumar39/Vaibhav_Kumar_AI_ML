#13. Implement notifications in a Flask app using websockets to notify users of updates.

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading')  

@app.route('/')
def index():
    return render_template('notify.html')

@app.route('/send_notification', methods=['POST'])
def send_notification():
    message = request.form.get('message', 'New Notification!')
    socketio.emit('notification', {'message': message})
    return 'Sent!', 200

@socketio.on('connect')
def handle_connect():
    print('User connected')

if __name__ == '__main__':
    socketio.run(app, debug=True)