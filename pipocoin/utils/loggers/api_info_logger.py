from utils.loggers import default_logger


def log_authenticated_user(API):
    user = API.me()
    default_logger.log("Authenticated User", user)


def log_twitter_configuration(API):
    configuration = API.configuration()
    default_logger.log("Twitter Api Configuration", configuration)
