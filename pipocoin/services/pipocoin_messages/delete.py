def success_user_deleted(user):
    return f"""✅ Account successfully deleted. \n\n🤡 Deleted Id: {user.get_id()}"""


def fail_error_occurred():
    return "❌ An error occurred while trying to delete your account."


def fail_not_registered_user():
    return "❌ You aren't registered. Please create an account before delete it."
