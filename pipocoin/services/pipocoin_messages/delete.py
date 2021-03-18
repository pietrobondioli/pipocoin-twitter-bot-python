def success_user_deleted(user_id):
    return f"Account successfully deleted. Deleted Id: {user_id}"


def fail_not_registered_user():
    return "You aren't registered. Please create an account before delete it."
