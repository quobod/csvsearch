import colorama
from colorama import Fore, Back, Style


def error(arg=""):
    return "{}{}{}".format(Fore.RED, Style.BRIGHT, arg)


def warning(arg=""):
    return "{}{}{}".format(Fore.YELLOW, Style.BRIGHT, arg)


def success(arg=""):
    return "{}{}{}".format(Fore.GREEN, Style.BRIGHT, arg)


def custom(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;1;255;255;255m".format(r, g, b, text)


CONSOLE_MESSENGER_SWITCH = {
    "error": error,
    "warning": warning,
    "success": success,
    "custom": custom,
}
