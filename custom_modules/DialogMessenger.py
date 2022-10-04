import tkinter
from tkinter import messagebox as tkMessageBox


def error(title="title", message="message"):
    tkMessageBox.showerror(title, message)


def warning(title="title", message="message"):
    tkMessageBox.showwarning(title, message)


def success(title="title", message="message"):
    tkMessageBox.showinfo(title, message)


DIALOG_MESSENGER_SWITCH = {"error": error, "warning": warning, "success": success}
