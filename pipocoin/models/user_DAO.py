from database.db import db_connection
import models.pipocoin_sql_queries as sql_queries


def db_query(sql, data=None):
    with db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute(sql, data)
        db_connection.commit()
        return db_cursor


def fetch_all_users():
    db_cursor = db_query(sql_queries.SQL_FETCH_ALL_USERS)
    rows = db_cursor.fetchall()
    return rows


def fetch_user_by_id(twitter_id):
    db_cursor = db_query(sql_queries.SQL_FETCH_USER_BY_ID, (twitter_id,))
    row = db_cursor.fetchone()
    return row


def fetch_user_by_name(user_name):
    db_cursor = db_query(sql_queries.SQL_FETCH_USER_BY_NAME, (user_name,))
    row = db_cursor.fetchone()
    return row


def create_new_user(twitter_id, user_name):
    user = (twitter_id, user_name, 0.0)
    db_query(sql_queries.SQL_CREATE_NEW_USER, user)
    return fetch_user_by_id(twitter_id)


def delete_user(twitter_id):
    db_query(sql_queries.SQL_DELETE_USER, (twitter_id,))
    return twitter_id


def transfer_to_user(from_twitter_id, to_user_name, amount):
    transfer_from = (amount, from_twitter_id)
    db_query(sql_queries.SQL_DECREASE_USER_BALANCE_BY_ID, transfer_from)
    transfer_to = (amount, to_user_name)
    db_query(sql_queries.SQL_INCREASE_USER_BALANCE_BY_NAME, transfer_to)
    return fetch_user_by_id(from_twitter_id)


def add_money_to_user(twitter_id, amount):
    transaction = (amount, twitter_id)
    db_query(sql_queries.SQL_INCREASE_USER_BALANCE_BY_ID, transaction)
    return fetch_user_by_id(twitter_id)
