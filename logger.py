import customtkinter as ctk
import tkinter as tk

log_textbox = None
success_logs = []
error_logs = []

def set_log_textbox(textbox):
    global log_textbox
    log_textbox = textbox
    log_textbox.tag_configure("error", foreground="#ff4c4c")
    log_textbox.tag_configure("success", foreground="#32cd32")
    log_textbox.tag_configure("info", foreground="#00bfff")
    log_textbox.tag_configure("warning", foreground="#ffae42")

def save_log(text, tag="info"):
    global success_logs, error_logs
    if tag == "success":
        success_logs.append(text)
    elif tag == "error":
        error_logs.append(text)
    else:
        if log_textbox is not None:
            log_textbox.configure(state=tk.NORMAL)
            log_textbox.insert("end"," "+ text + "\n" + "\n",tag)
            log_textbox.configure(state=tk.DISABLED)
            log_textbox.see("end")


def log(text,tag="info"):
    if log_textbox is not None:
        log_textbox.configure(state=tk.NORMAL)
        log_textbox.insert("end"," "+ text + "\n" + "\n",tag)
        log_textbox.configure(state=tk.DISABLED)
        log_textbox.see("end")

def showSucess():
    for text in success_logs:
        log(text, tag="success")

def showError():
    for text in error_logs:
        log(text, tag="error")

def clearLog():
    log_textbox.configure(state=tk.NORMAL)
    log_textbox.delete("1.0", tk.END)
    log_textbox.configure(state=tk.DISABLED)
