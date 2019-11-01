from flask import Flask,jsonify,request,make_response,render_template
from flask_socketio import SocketIO,emit
from threading import Lock
import random
import urllib.parse

from flask_cors import *

# app = Flask(__name__)
# CORS(app, supports_credentials=True)
#定义flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
async_mode = None
socketio = SocketIO(app,async_mode=async_mode)
#跨域
CORS(app, supports_credentials=True, resources={r'/*'})

thread = None
thread_lock = Lock()


name='cyy'
age=0
@app.route('/map')
def index():
    return render_template('map.html')


@app.route("/", methods=['GET','POST'])
def receive():
    referrer = request.referrer
    parse = urllib.parse

    scheme = parse.urlsplit(referrer).scheme
    netloc = parse.urlsplit(referrer).netloc
    port=parse.urlsplit(referrer).port

    # data = request.get_json()
    response = make_response("OK!")
    # response.headers['Access-Control-Allow-Credentials'] = 'true'
    # response.headers['Access-Control-Allow-Origin'] = "{scheme}://{netloc}".format(scheme=scheme, netloc=netloc)
    # response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,x-token'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'

    # get方式
    global name
    global age
    name=request.args.get('name')
    age=request.args.get('age')
    print("receive successfully!")
    print(name)
    print(age)
    return response


@socketio.on('connect', namespace='/test_conn')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

def background_thread():
    while True:
        socketio.sleep(5)
        # t = random.randint(1, 100)
        socketio.emit('server_response',
                      {'data': age},namespace='/test_conn')
if __name__ == '__main__':
    socketio.run(app, debug=True)




# data = request.get_json()
# return Response(data=json.dumps({'ok': True}), mimetype='application/json')