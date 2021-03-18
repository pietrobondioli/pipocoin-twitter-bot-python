def success_tranferred(from_user, to_user, amount):
    return f"✅🪙 Successfully transferred {amount} $pipo from your wallet to {to_user.get_name()}."


def fail_error_occurred():
    return "❌ An error occurred while trying to transfer $pipo."


def fail_not_registered_user():
    return "❌ You aren't registered. Please create an account to use $pipo bot."


def fail_not_registered_target_user():
    return "❌ The user you tried to transfer to aren't registered on $pipo bot."


def fail_not_enough_money_to_tranfer():
    return "❌ Not enough $pipo to transfer. Work harder."
