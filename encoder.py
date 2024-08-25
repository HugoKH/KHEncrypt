import random

class Encoder:
    def __init__(self) -> None:
        """
        Hash created at every new encode.
        Used to decode the given encoded message
        """
        self._input: str
        self._output: str = ""
        self._dict: dict = {}
        self._abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                    "_", " ", ",", "!", '"', "§", "$", "%", "&", "/", "(", ")", "=", "?", "´", "`", "+", "*", "~", "#", "'", "{", "[", "]", "}", "-", ".", ";",
                    "<", ">", "|", "^", "°"]
        
    def _create_hash(self):
        
        #letters that are still availabe for creating hash
        abc_still_availabe: list = []
        abc_still_availabe += self._abc

        for substr in self._abc:
            rnd_choice = random.choice(abc_still_availabe)
            abc_still_availabe.remove(rnd_choice)
            self._dict.setdefault(substr, rnd_choice)

        return self._dict
        
    def encode(self, input_str: str, save_path: str = None):
        """
        Returns tuple(encoded str, hash)\n
        If you want to save your encrypted string and hash to a txt, input path in save_path.
        If txt not exsistant, one will be created.
        Dont edit this txt, for the gui version to function
        """
        self._dict = {}
        hash = Encoder._create_hash(self)
        output: str = ""
        output_hash: str = ""
        
        for substr in input_str:
            output += (hash[substr])
            
        for key, value in hash.items():
            output_hash += (value)

        if save_path != None:
            try:
                with open(save_path, "a", encoding="utf-8") as datei:
                    datei.write(f"\nencrypted_str = {output}\nhash = {output_hash}\n")
            except OSError:
                print("No file path given")

        return output, output_hash
    
    def decode(self, input: str, hash: list):
        """
        Returns decoded str
        """
        decode_hash: dict = {}
        hash_index_counter: int = 0

        for substr in self._abc:
            decode_hash.setdefault(substr, hash[hash_index_counter])
            hash_index_counter += 1
        output: str = ""

        for substr in input:
            output += Tools.get_key_from_value(decode_hash, substr)
            
        return output
        
class Tools:
    def __init__(self) -> None:
        pass
    
    def get_key_from_value(d: dict, target_value):
        for key, value in d.items():
            if value == target_value:
                return key
        return None  # Return None if the value is not found