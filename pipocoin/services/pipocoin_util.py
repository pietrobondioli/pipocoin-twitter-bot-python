from models import user_DAO


def does_user_exists_by_id(user):
    return bool(user_DAO.fetch_user_by_id(user.get_id()))


def does_user_exists_by_name(user):
    return bool(user_DAO.fetch_user_by_name(user.get_name()))


def user_has_enough_money_by_id(user, amount):
    user = user_DAO.fetch_user_by_id(user.get_id())
    return bool(user.get_balance() >= float(amount))
