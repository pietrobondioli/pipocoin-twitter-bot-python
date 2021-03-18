import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        return conn
    except Error as e:
        print(e)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_db():
    DATABASE = "pipocoin.db"
    SQL_CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS user (
                                    twitter_id text NOT NULL UNIQUE PRIMARY KEY,
                                    user_name text NOT NULL UNIQUE,
                                    balance float NOT NULL
                                    );"""

    conn = create_connection(DATABASE)
    if conn is not None:
        create_table(conn, SQL_CREATE_USER_TABLE)
        conn.row_factory = sqlite3.Row
        return conn
    else:
        print("Error! cannot create the database connection.")


db_connection = create_db()
