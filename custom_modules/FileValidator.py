import os


def file_exists(filePath):
    return os.path.exists(filePath)


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def is_symlink(path):
    return os.path.islink(path)
