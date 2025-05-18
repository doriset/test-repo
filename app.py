from flask import Flask, jsonify
import platform
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my simple API!",
        "status": "running",
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "python_version": platform.python_version()
    })

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}! This is a simple Flask app."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)