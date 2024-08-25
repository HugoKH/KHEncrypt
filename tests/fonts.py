import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Available Fonts")

# Liste aller verfügbaren Schriftarten abrufen
available_fonts = list(font.families())

# Label erstellen, um die Schriftarten anzuzeigen
label = tk.Label(root, text="Verfügbare Schriftarten:", font=("Arial", 14))
label.pack(pady=10)

# Listbox erstellen, um die Schriftarten anzuzeigen
listbox = tk.Listbox(root, width=50, height=20)
listbox.pack(pady=20)

# Schriftarten zur Listbox hinzufügen
for f in available_fonts:
    listbox.insert(tk.END, f)

root.mainloop()