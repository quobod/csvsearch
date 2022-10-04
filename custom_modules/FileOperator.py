import os
from .FileValidator import fileExists, isFile
from .TypeTester import arg_is_a_list as aial
from .PlatformConstants import LINE_SEP as lsep


def delete_file(file_path):
    if fileExists(file_path) and isFile(file_path):
        os.remove(file_path)
        return not fileExists(file_path)


def append_list_to_file(file_path, list_data):
    if aial(list_data):
        file_exists = fileExists(file_path)
        is_file = isFile(file_path)

        if file_exists and is_file:
            with open(file_path, "a", 2) as f:
                for d in list_data:
                    str_d = "{}{}".format(str(d), lsep)
                    f.write(str_d)

            return fileExists(file_path)
        else:
            with open(file_path, "a", 2) as f:
                for d in list_data:
                    str_d = "{}{}".format(str(d), lsep)
                    f.write(str_d)

            return fileExists(file_path)
    return None


def write_list_to_file(file_path, list_data):
    if aial(list_data):
        file_exists = fileExists(file_path)
        is_file = isFile(file_path)

        if file_exists and is_file:
            deleted = delete_file(file_path)

            if deleted:
                with open(file_path, "w", 2) as f:
                    for d in list_data:
                        str_d = "{}{}".format(str(d), lsep)
                        f.write(str_d)

            return fileExists(file_path)
        else:
            with open(file_path, "w", 2) as f:
                for d in list_data:
                    str_d = "{}{}".format(str(d), lsep)
                    f.write(str_d)

            return fileExists(file_path)
    return None


def save_new_file(file_path, data=None):
    if not data == None:
        if fileExists(file_path) and isFile(file_path):
            deleted = delete_file(file_path)

            if deleted:
                with open(file_path, "w") as f:
                    f.write(data)

                return fileExists(file_path)
        else:
            with open(file_path, "w") as f:
                f.write(data)

            return fileExists(file_path)
    return None


def write_to_file(file_path, _data=None):
    if not _data == None:
        _string_data = str(_data)

        if fileExists(file_path):
            deleted = delete_file(file_path)

            if deleted:
                with open(file_path, "w") as f:
                    f.write(_string_data)

        else:
            with open(file_path, "w") as f:
                f.write(_string_data)

        return fileExists(file_path)


def append_to_file(file_path, _data=None):
    if not _data == None:
        _string_data = str(_data)

        if fileExists(file_path):
            with open(file_path, "a") as f:
                f.write(_string_data)
        else:
            with open(file_path, "w") as f:
                f.write(_string_data)

        return fileExists(file_path)
