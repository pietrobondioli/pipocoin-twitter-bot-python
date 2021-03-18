def success_get_stats(user):
    return f"✅ Successfully get stats.\n\n👤 Id: {user.get_id()}\n" \
        + f"🤡 Username: {user.get_name()}\n🪙 Balance: {user.get_balance()}"


def fail_error_occurred():
    return "❌ An error occurred while trying to get your stats."


def fail_not_registered_user():
    return "❌ You aren't registered. Please create an account to use $pipo bot."
