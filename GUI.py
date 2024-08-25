import tkinter as tk
import encoder as en

e = en.Encoder()

root = tk.Tk()
root.option_add("*Font", ("Consolas", 18))
root.title("GUI for KH encrypter")
root.geometry("350x240")

# Globale Variablen, um Fensterinstanzen zu speichern
str2encrypt_root = None
decrypt_root = None
decrypt_from_file_root = None

def str2encrypt():
    global str2encrypt_root
    if str2encrypt_root is None or not str2encrypt_root.winfo_exists():
        s2e = str2encrypt_root = tk.Toplevel(root)  # Verwende Toplevel statt Tk
        str2encrypt_root.title("String encryption")
        str2encrypt_root.geometry("800x400")
        str2encrypt_root.protocol("WM_DELETE_WINDOW", lambda: close_window("str2encrypt"))

        label = tk.Label(s2e, text="String to encrypt")
        label.grid(row=0, column=0, padx=10, pady=10)

        entry = tk.Entry(s2e, width=30)
        entry.grid(row=1, column=0, padx=10, pady=10)

        button = tk.Button(s2e, text="encrypt", command=lambda: print(e.encode(entry.get(), entry_path.get())))
        button.grid(row=1, column=1, padx=10, pady=10) 

        label_path = tk.Label(s2e, text="If you want to save to file, input path here")
        label_path.grid(row=2, column=0, padx=10, pady=10) 

        entry_path = tk.Entry(s2e, width=30)
        entry_path.grid(row=3, column=0, padx=10, pady=10)

def decrypt():
    global decrypt_root
    if decrypt_root is None or not decrypt_root.winfo_exists():
        d = decrypt_root = tk.Toplevel(root)  # Verwende Toplevel statt Tk
        decrypt_root.title("String decryption")
        decrypt_root.geometry("800x400")
        decrypt_root.protocol("WM_DELETE_WINDOW", lambda: close_window("decrypt"))

        label_str = tk.Label(d, text="String to decrypt")
        label_str.grid(row=0, column=0, padx=10, pady=10)

        entry_str = tk.Entry(d, width=30)
        entry_str.grid(row=0, column=1, padx=10, pady=10)

        label_hash = tk.Label(d, text="Hash")
        label_hash.grid(row=1, column=0, padx=10, pady=10)

        entry_hash = tk.Entry(d, width=30)
        entry_hash.grid(row=1, column=1, padx=10, pady=10)

        button = tk.Button(d, text="decrypt", command=lambda: print(e.decode(entry_str.get(), entry_hash.get())))
        button.grid(row=0, column=2, padx=10, pady=10)  

"""def decrypt_ff():
    global decrypt_from_file_root
    if decrypt_from_file_root is None or not decrypt_from_file_root.winfo_exists():
        decrypt_from_file_root = tk.Toplevel(root)  # Verwende Toplevel statt Tk
        decrypt_from_file_root.title("String decryption from file")
        decrypt_from_file_root.geometry("600x400")
        decrypt_from_file_root.protocol("WM_DELETE_WINDOW", lambda: close_window("decrypt_ff"))"""

def close_window(window_name):
    global str2encrypt_root, decrypt_root, decrypt_from_file_root
    if window_name == "str2encrypt":
        str2encrypt_root.destroy()
        str2encrypt_root = None
    elif window_name == "decrypt":
        decrypt_root.destroy()
        decrypt_root = None
    elif window_name == "decrypt_ff":
        decrypt_from_file_root.destroy()
        decrypt_from_file_root = None

str2encrypt_button = tk.Button(root, text="encrypt", command=str2encrypt, padx=80, pady=5)
str2encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="decrypt", command=decrypt, padx=80, pady=5)
decrypt_button.pack(pady=10)

"""decrypt_from_file_button = tk.Button(root, text="decrypt from file", command=decrypt_ff, padx=16, pady=5)
decrypt_from_file_button.pack(pady=10)"""

root.mainloop()
