from flask import Flask,jsonify,request
from flask_socketio import SocketIO,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
async_mode = None
socketio = SocketIO(app,async_mode=async_mode)

@app.route("/", methods=['GET','POST'])
def receive():
    data = request.get_json()

    #post方式：
    # name=request.form.get('name')
    # age=request.form.get('age')

    #get方式
    name=request.args.get('name')
    age=request.args.get('age')

    print("receive successfully!")
    print(name)
    print(age)
    # print(data)
    return 'OK!'

# data = request.get_json()
# return Response(data=json.dumps({'ok': True}), mimetype='application/json')

# if __name__ == '__main__':
#     socketio.run(app, debug=True)