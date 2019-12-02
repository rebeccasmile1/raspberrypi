from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO,emit
from threading import Lock
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


#定义socketio
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
async_mode = None
socketio = SocketIO(app,async_mode=async_mode)

thread = None
thread_lock = Lock()

@app.route('/')
def index():
    return render_template('map.html')

@socketio.on('connect', namespace='/test_conn')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

def background_thread():
    while True:
        socketio.sleep(5)
        t = random.randint(1, 100)
        socketio.emit('server_response',
                      {'data': t},namespace='/test_conn')

# if __name__ == '__main__':
#     socketio.run(app, debug=True)