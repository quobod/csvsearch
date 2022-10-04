import sys, os, datetime

from .PlatformConstants import LINE_SEP as lsep, platform as pltf
from .ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from .TypeTester import arg_is_a_dict as aiad, arg_is_a_list as aial

date = datetime.datetime.now()


def exit_prog(exit_code=0):
    sys.exit(exit_code)


def clear_screen():
    platform = pltf.platform()
    if "windows" not in platform and "microsoft" not in platform:
        os.system("clear")
    else:
        os.system("cls")
    exit_prog()


def verify_bt():
    results = os.system("hcitool dev")
    return results == 0


def am_pm():
    return date.strftime("%p")


def time_zone():
    return date.strftime("%Z")


def msecond():
    return date.strftime("%f")


def second():
    return date.strftime("%S")


def minute():
    return date.strftime("%M")


def hour():
    return date.strftime("%H")


def ihour():
    return date.strftime("%I")


def day_of_year():
    return date.strftime("%j")


def day_of_month():
    return date.strftime("%d")


def month():
    return date.strftime("%B")


def smonth():
    return date.strftime("%b")


def nmonth():
    return date.strftime("%m")


def weekday():
    return date.strftime("%A")


def sweekday():
    return date.strftime("%a")


def nweekday():
    return date.strftime("%w")


def year():
    return date.strftime("%Y")


def syear():
    return date.strftime("%y")


def week_of_year():
    return date.strftime("%U")


def time_stamp():
    return "{}:{}:{}".format(hour(), minute(), second())


def numbered_date_stamp():
    return "{}/{}/{}".format(year(), nmonth(), nweekday())


def numbered_date_stamp_f():
    return "{}/{}/{}".format(nweekday(), nmonth(), year())


def named_date_stamp():
    return "{}/{}/{}".format(year(), month(), nweekday())


def named_date_stamp_f():
    return "{}/{}/{}".format(nweekday(), month(), year())


def numbered_date_time_stamp():
    return "{}/{}/{},{}:{}:{}".format(
        year(), nmonth(), nweekday(), hour(), minute(), second()
    )
