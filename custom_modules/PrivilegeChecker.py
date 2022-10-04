import os


def is_user_root():
    return os.getuid() == 0


def get_logged_in_user():
    return os.getlogin()
