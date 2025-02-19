from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def get_code():
    return "0000"

@app.route('/plus/<int:a>/<int:b>', methods=['GET'])
def plus(a, b):
    return str(a + b), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
