#! /usr/bin/python3

import argparse

from pkg_resources import require

from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.Utils import exit_prog
from custom_modules.FileDialog import open_file_type
from custom_modules.FileValidator import file_exists
from custom_modules.FileInter import get_extension
from custom_modules.CsvReader import search_csv_file_thread as search_csv
from custom_modules.PlatformConstants import LINE_SEP as lsep


cus = cms["custom"]
desc = "This program searches CSV, JSON and TXT files for login credentials."
epil = "Search files containing login data. Use a file dialog or provide absolute file path."
vers = "%prog 0.1"


def error_handler(*args):
    cus = cms["custom"]
    arg = args[0]
    cargs = cus(254, 60, 60, arg)
    print("{}".format(cargs))
    exit_prog()


parser = argparse.ArgumentParser(description=desc, epilog=epil)
parser.error = error_handler
parser.version = vers
group = parser.add_mutually_exclusive_group()

group.add_argument(
    "-f",
    "--file",
    dest="file",
    nargs=1,
    help="Indicates the file path from standard input. Used with the search option.",
)

group.add_argument(
    "-d",
    "--dia",
    dest="dia",
    action="store_true",
    help="Indicates the file path from file dialog. Used with the search option.",
)

parser.add_argument(
    "-p", "--print", action="store_true", help="Print the entire document."
)

parser.add_argument(
    "-s", "--search", nargs=1, help="Search the document for given search term."
)

args = parser.parse_args()

keyword = None
file_path = None
file_ext = None
file_type = (
    "csv files",
    "*.csv",
)


def handle_std_input(cus, args, keyword, file_type):
    file_path = args.file[0]

    if file_exists(file_path):
        file_ext = get_extension(file_path)
        if file_ext == ".csv":
            print(
                "Keyword: {}\nFile Type: {}\nFile Path: {}{}".format(
                    keyword, file_type, file_path, lsep
                )
            )

            results = search_csv(file_path, keyword)
            status = results["status"]

            if status:
                data = results["data"]
                print(*data, sep=lsep)
        else:
            e_msg_header = cus(255, 133, 133, "Error")
            e_msg_body = cus(
                255,
                255,
                255,
                "Expected a .csv file but received a '{}' file".format(file_ext),
            )
            e_msg = "{} {}{}".format(e_msg_header, e_msg_body, lsep)
            print("{}".format(e_msg))


def handle_file_dialog(keyword, file_type):
    file_path = open_file_type(file_type)

    if file_path:
        print(
            "Keyword: {}\nFile Type: {}\nFile Path: {}\nFile Dialog{}".format(
                keyword, file_type, file_path, lsep
            )
        )

        results = search_csv(file_path, keyword)
        status = results["status"]

        if status:
            data = results["data"]
            print(*data, sep=lsep)


try:
    if args.search:
        keyword = args.search[0]

        if args.dia:
            handle_file_dialog(keyword, file_type)
        elif args.file:
            handle_std_input(cus, args, keyword, file_type)
    exit_prog()
except ValueError as ve:
    print(ve)
    exit_prog()
