# INSTRUCTIONS FOR USE
# The encrypted json file is stored in pwd.txt - the key for decryption is stored elsewhere remotely
# In order to view the decrypted json file, locate the key string, and execute python decrypt.py <key>
# This will write a decrypted pwd.json file to this directoy - use this to add or modify credentials
# Then re-encrypt pwd.json by executing python encrypt.py <key>
# Delete the unencrypted pwd.json file, and the newly encrypted string will be stored in pwd.txt

import sys
import json
from cryptography.fernet import Fernet

key = str.encode(sys.argv[1])
cipher_suite = Fernet(key)

with open('pwd.txt', 'r') as f:
    encrypted_byte_string = str.encode(f.read())

decrypted_txt = cipher_suite.decrypt(encrypted_byte_string).decode() # string representation
decrypted_dict = json.loads(decrypted_txt) #dict representation

with open('pwd.json', 'w', encoding='utf-8') as f:
    json.dump(decrypted_dict, f, ensure_ascii=False, indent=4)