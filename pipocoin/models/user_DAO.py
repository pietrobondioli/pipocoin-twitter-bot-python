from database.db import db_connection
import models.user_sql_queries as sql_queries
from models.user_model import User


def db_query(sql, data=None):
    with db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute(sql, data)
        db_connection.commit()
        return db_cursor


def fetch_all_users():
    db_cursor = db_query(sql_queries.SQL_FETCH_ALL_USERS)
    rows = db_cursor.fetchall()
    users = []
    for row in rows:
        user = User(row["twitter_id"], row["user_name"], row["balance"])
        users.append(user)
    return users


def fetch_user_by_id(user_id):
    db_cursor = db_query(sql_queries.SQL_FETCH_USER_BY_ID, (user_id,))
    row = db_cursor.fetchone()
    user = None
    if row:
        user = User(row["twitter_id"], row["user_name"], row["balance"])
    return user


def fetch_user_by_name(user_name):
    db_cursor = db_query(sql_queries.SQL_FETCH_USER_BY_NAME, (user_name,))
    row = db_cursor.fetchone()
    user = None
    if row:
        user = User(row["twitter_id"], row["user_name"], row["balance"])
    return user


def create_new_user(user):
    new_user = (user.get_id(), user.get_name(), 0.0)
    db_query(sql_queries.SQL_CREATE_NEW_USER, new_user)
    return fetch_user_by_id(user.get_id())


def delete_user(user):
    db_query(sql_queries.SQL_DELETE_USER, (user.get_id(),))


def transfer_to_user(from_user, to_user, amount):
    transfer_from = (amount, from_user.get_id())
    db_query(sql_queries.SQL_DECREASE_USER_BALANCE_BY_ID, transfer_from)
    transfer_to = (amount, to_user.get_name())
    db_query(sql_queries.SQL_INCREASE_USER_BALANCE_BY_NAME, transfer_to)
    return fetch_user_by_id(from_user.get_id())


def add_money_to_user(user, amount):
    transaction = (amount, user.get_id())
    db_query(sql_queries.SQL_INCREASE_USER_BALANCE_BY_ID, transaction)
    return fetch_user_by_id(user.get_id())
