from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/api/get_messages', methods = ['POST'])
def get_messages():
    json = request.get_json()
    if json['user'] == "larry":
        return jsonify({'messages':['test1', 'test2']})

    return jsonify({'error':'no user found'})

if __name__ == '__main__':
    app.run(debug = True)
