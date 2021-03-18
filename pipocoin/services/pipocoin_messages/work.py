def success_worked(user, amount):
    return f"✅🛠️ You earned {amount} $pipo. Your balance: {user.get_balance()} $pipo"


def fail_error_occurred():
    return "❌ An error occurred while trying to work. (Work Accident)"


def fail_not_registered_user():
    return "❌ You aren't registered. Please create an account to use $pipo bot."
