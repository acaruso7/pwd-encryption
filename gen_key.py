from cryptography.fernet import Fernet

key = Fernet.generate_key()
key_file = open("key.txt", "w")
key_file.write(key.decode())
key_file.close()
