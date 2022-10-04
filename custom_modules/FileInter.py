from pathlib import PurePath


def get_extension(file_path):
    return PurePath(file_path).suffix


def get_name(file_path):
    return PurePath(file_path).stem


def get_full_name(file_path):
    return PurePath(file_path).name


def get_parent_dir(file_path):
    return PurePath(file_path).parent


def get_parents_dir(file_path):
    return PurePath(file_path).parents


def get_file_uri(file_path):
    return PurePath(file_path).as_uri()
