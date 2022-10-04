import csv
from multiprocessing.pool import ThreadPool
from tkinter.tix import ROW
from .PlatformConstants import LINE_SEP as lsep


def search_csv_file(file_path, keyword):
    found = []

    with open(file_path, newline="") as f:
        line = csv.reader(f, delimiter=",", quotechar='"')

        for row in line:
            url = row[0]
            uname = row[1]
            pwd = row[2]

            if keyword in url or keyword in uname:
                found.append(
                    "URL: {}{}Username: {}{}Password: {}{}".format(
                        url, lsep, uname, lsep, pwd, lsep
                    )
                )

        return {"status": len(found) > 0, "data": found}


def print_csv_file(file_path):
    with open(file_path, newline="") as f:
        line = csv.reader(f, delimiter=",", quotechar='"')

        for row in line:
            print("{}".format(ROW))


def search_csv_file_thread(file_path, keyword, num_of_processes=3):
    pool = ThreadPool(processes=num_of_processes)
    async_results = pool.apply_async(search_csv_file, (file_path, keyword))
    return async_results.get()
