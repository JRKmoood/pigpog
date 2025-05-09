import tkinter as tk
import os
import ctypes
import webbrowser
import random
import time
import threading

timer = 0

def fenster_schliessen():
    fenster.destroy()

def button_rot_ausblenden():
    button_rot.pack_forget()
    label.config(text="roter Button ausgeblendet")

def countdown(zeit):
    if zeit > 0:
        label.config(text=str(zeit))
        fenster.after(1000, countdown, zeit - 1)
    else:
        fenster_schliessen()

def button_rot_anzeigen():
    button_rot.pack(pady=0)
    label.config(text="roter Button eingeblendet")

def fenster_minimieren():
    fenster.iconify()

def rechner_herunterfahren():
    label.config(text="Rechner wird heruntergefahren")

def minimize_windows():
    def enum_windows_proc(hwnd, lParam):
        if ctypes.windll.user32.IsWindowVisible(hwnd):
            ctypes.windll.user32.ShowWindow(hwnd, 6)
        return True

    ctypes.windll.user32.EnumWindows(
        ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.POINTER(ctypes.c_int))(enum_windows_proc),
        0
    )

def open_google_browser():
    webbrowser.open("https://chatgpt.com/")


def open_google():
    webbrowser.open("https://scoolcode.com/ide/679a2e4ca60b4422652c15d2?origin=https%3A%2F%2Fmy.logiscool.com%2Fapp%2Fproject%2F679a2e4ca60b4422652c15d2")

def open_neu_fenster():
    neu_fenster = tk.Toplevel(fenster)
    neu_fenster.title("Neues Fenster")
    neu_fenster.geometry("800x600")
    neu_fenster.config(bg="black")

    label_neu = tk.Label(neu_fenster, text="", font=("Helvetica", 48), fg="white", bg="black")
    label_neu.pack(pady=20)

    button_gelb_neu = tk.Button(neu_fenster, text="Neues Fenster öffnen", command=open_neu_fenster, width=20, height=2, bg="yellow", fg="black")
    button_gelb_neu.pack(pady=20)

    button_gruen_neu = tk.Button(neu_fenster, text="Grüner Button", command=button_rot_anzeigen, width=20, height=2, bg="green", fg="white")
    button_gruen_neu.pack(pady=20)

    button_rot_neu = tk.Button(neu_fenster, text="EXIT", command=lambda: countdown(timer), width=20, height=2, bg="red", fg="white")
    button_rot_neu.pack(pady=20)

    button_minimieren_neu = tk.Button(neu_fenster, text="Fenster minimieren", command=fenster_minimieren, width=20, height=2, bg="blue", fg="white")
    button_minimieren_neu.pack(pady=20)

    button_orange_neu = tk.Button(neu_fenster, text="Alle Fenster minimieren", command=minimize_windows, width=20, height=2, bg="orange", fg="white")
    button_orange_neu.pack(pady=20)

    button_google_neu = tk.Button(neu_fenster, text="logiscool Rechner open", command=open_google, width=20, height=2, bg="purple", fg="white")
    button_google_neu.pack(pady=20)

fenster = tk.Tk()
fenster.title("Mein Fenster")
fenster.geometry("800x600")
fenster.config(bg="black")

label = tk.Label(fenster, text="", font=("Helvetica", 48), fg="white", bg="black")
label.pack(pady=20)

button_gelb = tk.Button(fenster, text="Neues Fenster öffnen", command=open_neu_fenster, width=20, height=2, bg="yellow", fg="black")
button_gelb.pack(pady=20)

button_gruen = tk.Button(fenster, text="Grüner Button", command=button_rot_anzeigen, width=20, height=2, bg="green", fg="white")
button_gruen.pack(pady=20)

button_rot = tk.Button(fenster, text="EXIT", command=lambda: countdown(timer), width=20, height=2, bg="red", fg="white")
button_rot.pack(pady=20)

button_minimieren = tk.Button(fenster, text="Fenster minimieren", command=fenster_minimieren, width=20, height=2, bg="blue", fg="white")
button_minimieren.pack(pady=20)

button_orange = tk.Button(fenster, text="Alle Fenster minimieren", command=minimize_windows, width=20, height=2, bg="orange", fg="white")
button_orange.pack(pady=20)

button_google = tk.Button(fenster, text="logiscool Rechner open", command=open_google, width=20, height=2, bg="purple", fg="white")
button_google.pack(pady=20)


# Beispiel für einen neuen Button, der Google öffnet
button_google_browser = tk.Button(fenster, text="chatgipiti", command=open_google_browser, width=20, height=2, bg="blue", fg="white")
button_google_browser.pack(pady=20)

import tkinter as tk
import threading
import time
import pyautogui

# Variable um den Auto-Clicker Status zu speichern
auto_clicker_active = False

# Funktion für den Auto-Clicker
def auto_clicker():
    while auto_clicker_active:
        pyautogui.click()  # Mausklick ausführen
        time.sleep(0.1)  # Kurze Pause, um den Klick nicht zu schnell hintereinander zu machen

# Funktion zum Umschalten des Auto-Clickers
def toggle_auto_clicker():
    global auto_clicker_active
    if auto_clicker_active:
        auto_clicker_active = False
        button.config(text="Auto-Clicker Starten")
    else:
        auto_clicker_active = True
        button.config(text="Stoppen")
        # Thread ohne Verzögerung starten
        threading.Thread(target=auto_clicker, daemon=True).start()

# Fenster erstellen
root = tk.Tk()
root.title("Auto-Clicker")

# Button erstellen
button = tk.Button(root, text="Auto-Clicker Starten", command=toggle_auto_clicker)
button.pack(pady=20)

# GUI starten
root.mainloop()


fenster.mainloop()
