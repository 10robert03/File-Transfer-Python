import socket
import sys
import os

if len(sys.argv) < 3:
	print("IP or Port missing.")
	sys.exit(1)
else:
	ip = sys.argv[1]
	port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))
s.listen(1)
s.settimeout(10)

conn, addr = s.accept()
header = conn.recv(1024).decode().strip()
filename,  filesize = header.split(":")
filesize = int(filesize)
conn.send("Ok".encode())

with open("received_" + filename, "wb") as f:
	bytes_received = 0
	while bytes_received < filesize:
		chunk = conn.recv(4096)
		
		if not chunk:
			print(f"File '{filename}' received")
			break
		
		f.write(chunk)
		bytes_received += len(chunk)

conn.close()
s.close()
