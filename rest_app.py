import os
import signal

from flask import Flask, request, jsonify
from db_connector import get_user, create_user, update_user, delete_user

app = Flask(__name__)

@app.route('/stop_server', methods=['GET'])
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server shutting down...'

@app.route('/users/<user_id>', methods=['POST'])
def create_user_endpoint(user_id):
    data = request.json
    user_name = data.get('user_name')
    try:
        create_user(user_id, user_name)
        return jsonify({"status": "ok", "user_added": user_name}), 200
    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500

@app.route('/users/<user_id>', methods=['GET'])
def get_user_endpoint(user_id):
    user_name = get_user(user_id)
    if user_name:
        return jsonify({"status": "ok", "user_name": user_name}), 200
    else:
        return jsonify({"status": "error", "reason": "no such id"}), 500

@app.route('/users/<user_id>', methods=['PUT'])
def update_user_endpoint(user_id):
    data = request.json
    user_name = data.get('user_name')
    try:
        update_user(user_id, user_name)
        return jsonify({"status": "ok", "user_updated": user_name}), 200
    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_endpoint(user_id):
    try:
        delete_user(user_id)
        return jsonify({"status": "ok", "user_deleted": user_id}), 200
    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        db_user = sys.argv[1]
        db_pass = sys.argv[2]
    else:
        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASS']
    app.run(debug=True)
