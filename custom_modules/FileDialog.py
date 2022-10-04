from email import message
import tkinter as tk
from tkinter import filedialog as fd
from .PlatformConstants import CUR_DIR as cdir
from .TypeTester import arg_is_a_tuple as aiat, arg_is_a_string as aias
from .ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

root = tk.Tk()
root.title("Open File")
root.resizable(False, False)
root.geometry("300x150")
root.withdraw()
cus = cms["custom"]


def open_file():
    types = (("All files", "*.*"),)

    filename = fd.askopenfilename(title="Open files", initialdir=cdir, filetypes=types)

    return filename


def open_file_type(
    file_type=("All files", "*.*"),
):
    if aiat(file_type):
        types = (file_type,)

        filename = fd.askopenfilename(
            title="Open files", initialdir=cdir, filetypes=types
        )

        return filename
    else:
        if file_type == None:
            received = "nothing"
        elif aias(file_type):
            if len(file_type) == 0:
                received = "nothing"
            else:
                received = "[{}]".format(type(file_type))
        else:
            received = "[{}]".format(type(file_type))
        e_msg_header = cus(255, 110, 110, "Error")
        e_msg_body = cus(
            255,
            255,
            255,
            "Expected a tuple parameter but received {}".format(received),
        )
        e_msg = "{} {}".format(e_msg_header, e_msg_body)
        raise ValueError(e_msg)
