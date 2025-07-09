import customtkinter as ctk
import tkinter as tk
import logger
import Sorter

# Ustawienia stylu
ctk.set_appearance_mode("dark")  # albo "dark"
ctk.set_default_color_theme("green")

# Tworzymy okno
root = ctk.CTk()
root.title("Sortownica zwyczajna")
root.geometry("800x800")

# ---------------------------------------------------
# Nagłówek
header = ctk.CTkFrame(root)
header.grid(row=0, column=0, sticky="nsew")
header_label = ctk.CTkLabel(header, text="Sortownica zwyczajna", font=("Segoe UI", 20))
header_label.pack(pady=10)

# ---------------------------------------------------
# Środkowy panel (podzielony na górny , środkowy, dolny)
middle = ctk.CTkFrame(root)
middle.grid(row=1, column=0, sticky="nsew")

middle.grid_rowconfigure(0, weight=1)   # górny panel
middle.grid_rowconfigure(1, weight=2)   #środkowy
middle.grid_rowconfigure(2, weight=1)   # dolny panel (więcej miejsca na logi)
middle.grid_columnconfigure(0, weight=1)

# ---------------------------------------------------
# Górny panel z przyciskiem
middle_up = ctk.CTkFrame(middle)
middle_up.grid(row=0, column=0, sticky="nsew")

middle_up.grid_rowconfigure(0, weight=1)
middle_up.grid_columnconfigure(0, weight=1)

button_frame = ctk.CTkFrame(middle_up)
button_frame.grid(row=0, column=0, sticky="nsew")
button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure(0, weight=1)

button = ctk.CTkButton(button_frame, text="Sortuj!",command=Sorter.sort_dest, font=("Segoe UI", 16))
button.grid(row=0, column=0)

middle_mid = ctk.CTkFrame(middle)
middle_mid.grid(row=1, column=0, sticky="nsew")

middle_mid.grid_rowconfigure(0, weight=1)
middle_mid.grid_columnconfigure(0, weight=1)
btns_frame = ctk.CTkFrame(middle_mid)
btns_frame.grid(row=0, column=0, sticky="nsew")
btns_frame.grid_rowconfigure(0, weight=1)
btns_frame.grid_columnconfigure(0, weight=1)
btns_frame.grid_columnconfigure(1, weight=1)
btns_frame.grid_columnconfigure(2, weight=1)

btn_clear = ctk.CTkButton(
    btns_frame,
    text="Wyczyść",
    font=("Segoe UI", 16),
    fg_color="white",
    text_color="black",
    hover_color="#dcdcdc",
    command=logger.clearLog,

)
btn_success = ctk.CTkButton(btns_frame, text="Pokaż udane", command=logger.showSucess, font=("Segoe UI", 16))
btn_fail = ctk.CTkButton(
    btns_frame,
    text="Błąd",
    font=("Segoe UI", 16),
    fg_color="#d32f2f",      # mocny czerwony (zgodny z ciemnym trybem)
    hover_color="#9a1f1f",   # ciemniejszy czerwony na hover
    text_color="white",     # biały tekst dla kontrastu
    command=logger.showError,
)

btn_clear.grid(row=0, column=0)
btn_success.grid(row=0, column=1)
btn_fail.grid(row=0, column=2)


# ---------------------------------------------------
# Dolny panel na logi
middle_bottom = ctk.CTkFrame(middle)
middle_bottom.grid(row=2, column=0, sticky="nsew",padx=10,pady=10)

middle_bottom.grid_rowconfigure(0, weight=1)
middle_bottom.grid_columnconfigure(0, weight=1)


log_textbox = tk.Text(middle_bottom, font=("Consolas", 12), bg="#222222")

log_textbox = tk.Text(
    middle_bottom,
    font=("Consolas", 12),
    bg="#1f1f1f",
    fg="#e0e0e0",
    insertbackground="#e0e0e0",
    highlightthickness=0,
    borderwidth=1,
    relief="solid",
    wrap="word"
)

log_textbox.grid(row=0, column=0, sticky="nsew")

logger.set_log_textbox(log_textbox)

# Przykładowy tekst do logów
logger.save_log("Start programu...",tag="info")
logger.save_log("Error Test", tag="error")
logger.save_log("Warning Test", tag="warning")
logger.save_log("Info Test", tag="info")
logger.save_log("Success Test", tag="success")

# ---------------------------------------------------
# Stopka
footer = ctk.CTkFrame(root, height=40)
footer.grid(row=2, column=0, sticky="nsew")
footer_label = ctk.CTkLabel(footer, text="To jest stopka", font=("Segoe UI", 12))
footer_label.pack(pady=5)

# ---------------------------------------------------
# Konfiguracja wierszy i kolumn w root
root.grid_rowconfigure(0, weight=0)   # nagłówek
root.grid_rowconfigure(1, weight=1)   # środek
root.grid_rowconfigure(2, weight=0)   # stopka
root.grid_columnconfigure(0, weight=1)

root.mainloop()
