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
    "-j",
    "--json",
    dest="json",
    action="store_true",
    help="Indicates the file type is .json",
)

group.add_argument(
    "-c",
    "--csv",
    dest="csv",
    action="store_true",
    help="Indicates the file type is .csv",
)

group.add_argument(
    "-t",
    "--text",
    dest="text",
    action="store_true",
    help="Indicates the file type is .txt",
)

parser.add_argument("-f", "--file", nargs=1, help="The file to search")

parser.add_argument("-k", "--key", nargs=1, help="The search term", required=True)

args = parser.parse_args()

keyword = args.key[0]
file_type = None
file_path = None

if args.text:
    file_type = (
        "text files",
        "*.txt",
    )
if args.csv:
    file_type = (
        "csv files",
        "*.csv",
    )
if args.json:
    file_type = (
        "json files",
        "*.json",
    )

try:
    if not args.file:
        # If file type is not chosen, then default to .csv
        if not file_type:
            file_type = (
                "csv files",
                "*.csv",
            )

        # Check if user chose a file. If file was not chosen, exit the program.
        file_path = open_file_type(file_type)

        if file_path:
            print(
                "Keyword: {}\nFile Type: {}\nFile Path: {}\nFile Dialog{}".format(
                    keyword, file_type, file_path, lsep
                )
            )

            results = search_csv(file_path, keyword)

            if results["status"]:
                found = results["data"]
                print(*found, sep=lsep)
        else:
            exit_prog()
    elif args.file:
        # Check if file path exists
        file_path = args.file[0]

        if file_exists(file_path):
            # Filter the file for accepted types
            file_ext = get_extension(file_path)

            if file_ext != ".csv" and file_ext != ".json" and file_ext != ".txt":
                e_msg_header = cus(255, 110, 110, "Error")
                e_msg_body = cus(
                    255,
                    255,
                    255,
                    "Expected file types: .csv, .json or .txt, but received a {} file.".format(
                        file_ext
                    ),
                )
                e_msg = "{} {}".format(e_msg_header, e_msg_body)
                raise ValueError(e_msg)
            else:
                # Check and configure file type for display
                if file_ext == ".csv":
                    file_type = (
                        "csv files",
                        "*.csv",
                    )

                if file_ext == ".json":
                    file_type = (
                        "json files",
                        "*.json",
                    )

                if file_ext == ".txt":
                    file_type = (
                        "text files",
                        "*.txt",
                    )

                print(
                    "Keyword: {}\nFile Type: {}\nFile Path: {}{}".format(
                        keyword, file_type, file_path, lsep
                    )
                )

            results = search_csv(file_path, keyword)

            if results["status"]:
                found = results["data"]
                print(*found, sep=lsep)
            exit_prog()
    else:
        exit_prog()
except ValueError as ve:
    print(ve)
    exit_prog()
