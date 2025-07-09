import os
import shutil
import tkinter as tk
from pathlib import Path
import customtkinter as ctk

import logger
from logger import success_logs, error_logs

def sort_dest():
    print("Hello world!")
    logger.success_logs.clear()
    logger.error_logs.clear()
    desktop_path = Path.home() / "Desktop"
    sorted_folder = desktop_path / "Posortowane"
    print("Lokalizacja pulpitu: ", desktop_path)
    folders = [
        sorted_folder / "Tekstowe" / "PDF",
        sorted_folder / "Tekstowe" / "Edytowalne",
        sorted_folder / "Wideo",
        sorted_folder / "Zdjecia"
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
    print("Foldery utworzone")

    categories = {
        "Tekstowe/PDF": ["pdf"],
        "Tekstowe/Edytowalne": ["doc","docx","txt","odt","rtf"],
        "Wideo": ["mp4","avi","mkv","mov","gif"],
        "Zdjecia": ["jpg","jpeg","png","gif","bmp","tiff"]
    }

    for item in desktop_path.iterdir():
        if item.is_file():
            ext = item.suffix[1:].lower()

            moved = False
            for folder,extensions in categories.items():
                if ext in extensions:
                    taget = sorted_folder / folder / item.name
                    shutil.move(str(item),str(taget))
                    moved = True
                    logger.save_log(f"Przenesiono {item.name} do {folder}",tag="success")
                    break

        if not moved:
            logger.save_log(f"Pominięto {item.name}",tag="error")



    logger.save_log("Sortowanie zakonczone",tag="info")


def sort_test():
    logger.save_log("Sortowanie test", tag="info")