def success_worked(user, amount):
    balance = user["balance"]
    return f"You earned {amount} $pipo. Your balance: {balance} $pipo"


def fail_not_registered_user():
    return "You aren't registered. Please create an account to use $pipo bot."
