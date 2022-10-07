import csv
from multiprocessing.pool import ThreadPool
from threading import Thread
from tkinter.tix import ROW
from .PlatformConstants import LINE_SEP as lsep


def search_csv_file(file_path, keyword):
    found = []

    with open(file_path, newline="") as f:
        line = csv.reader(f, delimiter=",", quotechar='"')

        try:
            for row in line:
                if len(row) == 3:
                    url = row[0]
                    uname = row[1]
                    pwd = row[2]

                    if keyword in url or keyword in uname:
                        found.append(
                            "URL: {}{}Username: {}{}Password: {}{}".format(
                                url, lsep, uname, lsep, pwd, lsep
                            )
                        )

                elif len(row) == 4:
                    website = row[0]
                    url = row[1]
                    uname = row[2]
                    pwd = row[3]

                    if keyword in url or keyword in uname:
                        found.append(
                            "Website: {}{}URL: {}{}Username: {}{}Password: {}{}".format(
                                website, lsep, url, lsep, uname, lsep, pwd, lsep
                            )
                        )
                else:
                    print(row)
                    return {"status": False, "data": row}

        except csv.Error as cerr:
            pass

        return {"status": len(found) > 0, "data": found}


def print_csv_file(file_path):
    with open(file_path, newline="") as f:
        line = csv.reader(f, delimiter=",", quotechar='"')
        try:
            for row in line:
                print("{}".format(row))
        except csv.Error as cerr:
            pass


def search_csv_file_thread(file_path, keyword, num_of_processes=3):
    pool = ThreadPool(processes=num_of_processes)
    async_results = pool.apply_async(search_csv_file, (file_path, keyword))
    return async_results.get()


def print_csv_thread(file_path):
    print_thread = Thread(target=print_csv_file, args=(file_path,))
    print_thread.start()
    print_thread.join()
    print_thread = None
