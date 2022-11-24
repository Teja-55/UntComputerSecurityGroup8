
import socket

IP_ADDRESS = '10.125.226.248'
PORT = 68

print('Creating Socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((IP_ADDRESS, PORT))
	print('Listening for connections...')
	s.listen(1)
	conn, addr = s.accept()
	print(f'Connection from {addr} established!')
	with conn:
		while True:
			key = conn.recv(1024).decode()
			with open('symkey.key', 'a') as f:
				f.write(key+'\n')
			break
		print('Connection completed and closed')
