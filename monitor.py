from flask import Flask
from flask import render_template
import flask_cors as CORS

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
async_mode = None
CORS(app, supports_credentials=True, resources={r'/*'})

@app.route('/monitor')
def monitor():
    return render_template('monitor.html')


# if __name__ == '__main__':
#     app.run()