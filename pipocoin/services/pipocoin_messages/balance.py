def success_get_balance(user):
    return f"✅ Successfully get balance.\n\n🪙 Balance: {user.get_balance()}"


def fail_error_occurred():
    return "❌ An error occurred while trying to get your balance."


def fail_not_registered_user():
    return "❌ You aren't registered. Please create an account to use $pipo bot."
