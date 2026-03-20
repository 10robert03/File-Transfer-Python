import os
import sys
import socket
import time

if len(sys.argv) < 4:
	print("IP, path or port  missing")
	sys.exit(1)

receiver_ip = sys.argv[1]
path = sys.argv[2]
port = int(sys.argv[3])

if not os.path.exists(path):
	print(f"Path '{path}' does not exist")
	sys.exit(1)

filename = os.path.basename(path)
filesize = os.path.getsize(path)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
	try:
		s.connect((receiver_ip, port))
		print("Connected")
		break
	except:
		print("No connection possible")
		time.sleep(5)

header_content = f"{filename}:{filesize}"
header = header_content.ljust(1024).encode()
s.send(header)

if s.recv(1024).decode().strip() == "Ok":
	print(f"Sending {filename} ({filesize} bytes).")
	
	with open(path, "rb") as f:
		bytes_sent = 0
		while True:
			chunk = f.read(4096)
			if not chunk:
				print("File read.")
				break
		
			s.sendall(chunk)
			
			bytes_sent += len(chunk)
			percent = (bytes_sent/filesize) * 100
			print(f"\rProgress: {percent:.2f}%", end="")

	print("Transfer completed")
else:
	print("Header was not accepted")

s.close()

