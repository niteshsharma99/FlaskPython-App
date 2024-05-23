from flask import Flask, jsonify, request, send_from_directory
import socket
import os

app = Flask(__name__, static_folder='.')

@app.route('/api/info', methods=['GET'])
def get_info():
    hostname = socket.gethostname()
    ip_address = request.remote_addr
    return jsonify({
        'hostname': hostname,
        'ip_address': ip_address
    })

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

