#! /usr/bin/python3


from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.Utils import exit_prog
from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc
from custom_modules.FileValidator import file_exists as fe
from custom_modules.FileInter import get_extension as ge
from custom_modules.CsvReader import print_csv_thread as pct


if argsc == 1:
    file_path = args[0]

    print("File: {}".format(file_path))

    if fe(file_path) and ge(file_path) == ".csv":
        pct(file_path)


exit_prog()
