from models import pipocoin_dao


def does_user_exists_by_id(user_id):
    return bool(pipocoin_dao.fetch_user_by_id(user_id))


def does_user_exists_by_name(user_name):
    return bool(pipocoin_dao.fetch_user_by_name(user_name))


def user_has_enough_money(user_id, amount):
    user = pipocoin_dao.fetch_user_by_id(user_id)
    return bool(user["balance"] >= float(amount))
