import tkinter as tk
import encoder as en

e = en.Encoder()

class GUI():
    

    def __init__(self) -> None:
        self._root = tk.Tk()
        self._root.option_add("*Font", ("Consolas", 18))
        self._root.title("GUI for KH encrypter")
        self._root.geometry("350x240")

        self._str2encrypt_root = None
        self._decrypt_root = None
        self._decrypt_from_file_root = None

        str2encrypt_button = tk.Button(self._root, text="encrypt", command=lambda:GUI.str2encrypt(self), padx=80, pady=5)
        str2encrypt_button.pack(pady=10)

        decrypt_button = tk.Button(self._root, text="decrypt", command=lambda:GUI.decrypt(self), padx=80, pady=5)
        decrypt_button.pack(pady=10)

        decrypt_from_file_button = tk.Button(self._root, text="decrypt from file", command=lambda:GUI.decrypt_ff(self), padx=16, pady=5)
        decrypt_from_file_button.pack(pady=10)

        self._root.mainloop()

    def str2encrypt(self):
        #global str2encrypt_root
        if self._str2encrypt_root is None or not self._str2encrypt_root.winfo_exists():
            s2e = self._str2encrypt_root = tk.Toplevel(self._root)  # Verwende Toplevel statt Tk
            self._str2encrypt_root.title("String encryption")
            self._str2encrypt_root.geometry("800x400")
            self._str2encrypt_root.protocol("WM_DELETE_WINDOW", lambda: GUI.close_window(self, "str2encrypt"))

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

    def decrypt(self):
        #global decrypt_root
        if self._decrypt_root is None or not self._decrypt_root.winfo_exists():
            d = self._decrypt_root = tk.Toplevel(self._root)  # Verwende Toplevel statt Tk
            self._decrypt_root.title("String decryption")
            self._decrypt_root.geometry("800x400")
            self._decrypt_root.protocol("WM_DELETE_WINDOW", lambda: GUI.close_window(self, "decrypt"))

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

    def decrypt_ff(self):
        #global decrypt_from_file_root
        if self._decrypt_from_file_root is None or not self._decrypt_from_file_root.winfo_exists():
            dff = self._decrypt_from_file_root = tk.Toplevel(self._root)  # Verwende Toplevel statt Tk
            self._decrypt_from_file_root.title("String decryption from file")
            self._decrypt_from_file_root.geometry("800x400")
            self._decrypt_from_file_root.protocol("WM_DELETE_WINDOW", lambda: GUI.close_window(self, "decrypt_ff"))

            self._hash = tk.StringVar(dff)
            self._string = tk.StringVar(dff)

            self._hashes = [""]
            self._strings = [""]

            self._hash.set("loade erst!")
            self._string.set("loade erst!")

            label = tk.Label(dff, text="txt path")
            label.grid(row=0, column=0, padx=10, pady=10)

            entry_path = tk.Entry(dff, width=30)
            entry_path.grid(row=1, column=0, padx=10, pady=10)

            button = tk.Button(dff, text="load", command=lambda: GUI.get_data_from_txt(self, entry_path.get()))
            button.grid(row=1, column=1, padx=10, pady=10) 

            label_hashes = tk.Label(dff, text="hashes")
            label_hashes.grid(row=2, column=0, padx=10, pady=10) 

            self._option_hashes = tk.OptionMenu(dff, self._hash, *self._hashes)
            self._option_hashes.config(width=20)
            self._option_hashes.grid(row=3, column=0, padx=10, pady=10)

            label_Strings = tk.Label(dff, text="Strings")
            label_Strings.grid(row=2, column=1, padx=10, pady=10) 

            self._option_str = tk.OptionMenu(dff, self._string, *self._strings)
            self._option_str.config(width=10)
            self._option_str.grid(row=3, column=1, padx=10, pady=10)

            label_str_entry = tk.Label(dff, text="Input string")
            label_str_entry.grid(row=4, column=0, padx=10, pady=10) 

            self._entry_str_entry = tk.Entry(dff, width=30)
            self._entry_str_entry.grid(row=5, column=0, padx=10, pady=10)

            button_decrypt = tk.Button(dff, text="decrypt", command=lambda: print(e.decode(GUI.hash(self), self._hash.get())))
            button_decrypt.grid(row=5, column=1, padx=10, pady=10) 

    def hash(self):
        if self._entry_str_entry.get() != "":
            return self._entry_str_entry.get()
        else:
            return self._string.get()

    def close_window(self, window_name):
        #global str2encrypt_root, decrypt_root, decrypt_from_file_root
        if window_name == "str2encrypt":
            self._str2encrypt_root.destroy()
            self._str2encrypt_root = None
        elif window_name == "decrypt":
            self._decrypt_root.destroy()
            self._decrypt_root = None
        elif window_name == "decrypt_ff":
            self._decrypt_from_file_root.destroy()
            self._decrypt_from_file_root = None

    def get_data_from_txt(self, path: str):
        """
        Returns tuple (str, hash) both as a list values are parallel like a dict
        """
        encrypted_str: list = []
        hashes: list = []
        nextline_hash = False

        try:
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    stripped_line = line.strip()

                    if nextline_hash == True:
                        hashes.append(stripped_line[7:])
                        nextline_hash = False
                    
                    #print(encrypted_str)
                    if stripped_line != "":
                        if "encrypted_str = " in stripped_line[:16]:
                            encrypted_str.append(stripped_line[16:])
                            nextline_hash = True

        except OSError:
            print("file path not set correctly")

        self._hashes = hashes
        self._strings = encrypted_str
        update_option_menus(self)

def update_option_menus(self):
    """
    Updates the OptionMenu widgets with the new hashes and strings
    """
    menu = self._option_hashes['menu']
    menu.delete(0, 'end')
    for hash_value in self._hashes:
        menu.add_command(label=hash_value, command=tk._setit(self._hash, hash_value))

    menu = self._option_str['menu']
    menu.delete(0, 'end')
    for string_value in self._strings:
        menu.add_command(label=string_value, command=tk._setit(self._string, string_value))

gui = GUI()