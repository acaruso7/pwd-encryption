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

f = open('pwd.json')
data = json.load(f)
f.close()

# convert json to byte string, encrypt, and store in txt file
encrypted_txt = cipher_suite.encrypt(str.encode(json.dumps(data))).decode() #stored as string
text_file = open("pwd.txt", "w")
text_file.write(encrypted_txt)
text_file.close()



