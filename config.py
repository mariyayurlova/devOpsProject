import pymysql

DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user',
    'password': 'password',
    'db': 'db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}