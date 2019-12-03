from flask import Flask,jsonify,request,make_response,render_template


from flask_cors import *

# app = Flask(__name__)
# CORS(app, supports_credentials=True)
#定义flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

#跨域
CORS(app, supports_credentials=True, resources={r'/*'})
@app.route('/')
def monitor():
    return render_template('monitor.html')

@app.route('/video')
def video():
    return render_template('video.html')

if __name__ == '__main__':
    app.run()