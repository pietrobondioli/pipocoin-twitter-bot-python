def log(title, content):
    print('-------------------')
    print(title + ": ")
    print(content)
    print('-------------------')


def log_authenticated_user(API):
    user = API.me()
    log("Authenticated User", user)


def log_twitter_configuration(API):
    configuration = API.configuration()
    log("Twitter Api Configuration", configuration)
