import os
import signal

from flask import Flask
from db_connector import create_connection, get_user

app = Flask(__name__)

@app.route('/stop_server', methods=['GET'])
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server shutting down...'

@app.route('/users/get_user_data/<user_id>')
def get_user_data(user_id):
    conn = create_connection()
    user_name = get_user(user_id)
    try:
        if user_name:
            return f'<h1 id="user_name">{user_name}</h1>'
        else:
            return '<h1>Error: No such ID</h1>', 404
    finally:
        conn.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        db_user = sys.argv[1]
        db_pass = sys.argv[2]
    else:
        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASS']
    app.run(debug=True, port=5001)