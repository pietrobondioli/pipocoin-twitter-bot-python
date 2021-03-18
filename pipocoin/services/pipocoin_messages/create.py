def success_user_created(user):
    return f"✅Account successfully created.\n\n👤 Id: {user.get_id()}\n" \
        + f"🤡 Username: {user.get_name()}\n🪙 Balance: {user.get_balance()}"


def fail_error_occurred():
    return "❌ An error occurred while trying to create the account."


def fail_already_registered_user():
    return "❌ You are already registered."
