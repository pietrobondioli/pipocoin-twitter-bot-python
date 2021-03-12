def log_authenticated_user(API):
    user = API.me()
    print(user)
