import os
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

import customtkinter as ctk

import logger
from logger import success_logs, error_logs

categories = {
    "Tekstowe/PDF": ["pdf"],
    "Tekstowe/Edytowalne": ["doc", "docx", "txt", "odt", "rtf"],
    "Wideo": ["mp4", "avi", "mkv", "mov", "gif"],
    "Zdjecia": ["jpg", "jpeg", "png", "gif", "bmp", "tiff"],
    "Exe" : ["exe"]
}

def sort_dest(selected_categories):
    logger.success_logs.clear()
    logger.error_logs.clear()

    if "Exe" in selected_categories:
        confirm = messagebox.askyesno("UWAGA!", "Czy na pewno chcesz posortować pliki .exe?")
        if not confirm:
            logger.save_log("Sortowanie plików .exe anulowane przez użytkownika", tag="warning")
            selected_categories.remove("Exe")


    desktop_path = Path.home() / "Desktop"
    sorted_folder = desktop_path / "Posortowane"

    # Tworzenie folderów tylko dla wybranych kategorii
    for folder in selected_categories:
        (sorted_folder / folder).mkdir(parents=True, exist_ok=True)

    for item in desktop_path.iterdir():
        if item.is_file():
            ext = item.suffix[1:].lower()
            moved = False

            # Sprawdź czy plik pasuje do którejś wybranej kategorii
            for folder, extensions in categories.items():
                if folder not in selected_categories:
                    continue
                if ext in extensions:
                    target = sorted_folder / folder / item.name
                    shutil.move(str(item), str(target))
                    moved = True
                    logger.save_log(f"Przeniesiono {item.name} do {folder}", tag="success")
                    break

            if not moved:
                logger.save_log(f"Pominięto {item.name}", tag="error")

    logger.save_log("Sortowanie zakończone", tag="info")


def sort_test():
    logger.save_log("Sortowanie test", tag="info")