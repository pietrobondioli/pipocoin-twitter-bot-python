def success_user_created(user):
    user_name, balance = user["user_name"], user["balance"]
    return f"Account successfully created. Username: {user_name} Balance: {balance}"


def fail_already_registered_user():
    return "You are already registered."
