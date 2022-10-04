from . import PlatformConstants as platform
from .FileValidator import exists, is_dir, is_file, is_symLink


def read_file_to_console(path):
    if exists(path):
        with open(path) as file:
            for line in file:
                print("{}".format(line))

    else:
        raise FileExistsError("File path '{}' not found".format(path))


def read_file_to_list(path):
    if exists(path):
        list = []

        with open(path) as file:
            for line in file:
                list.append(line)

        return list
    else:
        raise FileExistsError("File path '{}' not found".format(path))


def read_file_to_dict(path):
    if exists(path):
        dict = {}
        list = []

        with open(path) as file:
            for line in file:
                list.append(line)

            for i, l in enumerate(list, start=1):
                dict.update({str(i): str(l)})

        return dict
    else:
        raise FileExistsError("File path '{}' not found".format(path))
