#12. Build a Flask app that updates data in real-time using WebSocket connections.
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC123'
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("live.html")

@app.route('/admin')
def admin():
    return render_template('admin.html')

@socketio.on('new_headline')
def handle_new_headline(data):
    print("New headline:", data['headline'])
    emit('broadcast_headline', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)