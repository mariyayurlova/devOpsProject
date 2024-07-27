import pymysql
from datetime import datetime

def create_connection():
    return pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='user',
        password='password',
        db='mydb',
        cursorclass=pymysql.cursors.DictCursor
    )

def create_user(user_id, user_name):
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, %s)",
                           (user_id, user_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            conn.commit()
    finally:
        conn.close()


def get_user(user_id):
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT user_name FROM users WHERE user_id=%s", (user_id,))
            result = cursor.fetchone()
            return result['user_name']
    finally:
        conn.close()

def update_user(user_name, user_id):
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users SET user_name=%s WHERE user_id=%s", (user_name, user_id))
            conn.commit()
    finally:
        conn.close()


def delete_user(user_id):
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
            conn.commit()
    finally:
        conn.close()

