import encoder as en
e = en.Encoder()

str_to_encode = input(f"Geben den zu verschlüsselnden str ein:")
path =r"C:\Users\hugts\Desktop\newpython\encrypter\tests\pimm.txt"

encoded_str, str_hash = e.encode(str_to_encode, path)
print(f"encoded str: '{encoded_str}'\noriginal str: '{str_to_encode}'\nhash: '{str_hash}'")
decoded_str = e.decode(encoded_str, str_hash)
print(f"decoded str: '{decoded_str}'")

encoded_str, str_hash = e.encode(str_to_encode, path)
print(f"encoded str: '{encoded_str}'\noriginal str: '{str_to_encode}'\nhash: '{str_hash}'")
decoded_str = e.decode(encoded_str, str_hash)
print(f"decoded str: '{decoded_str}'")

def get_data_from_txt(path: str = r"C:\Users\hugts\Desktop\newpython\encrypter\tests\pimm.txt"):
    """
    Returns tuple (str, hash) both as a list values are parallel like a dict
    """
    encrypted_str: list = []
    hashes: list = []
    nextline_hash = False

    try:
        with open(path, "r") as file:
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

    return encrypted_str, hashes

strr, hashh = get_data_from_txt()
print(strr[0]+" "+hashh[0])