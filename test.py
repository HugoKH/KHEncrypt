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