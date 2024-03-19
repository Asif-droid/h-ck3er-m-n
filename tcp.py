import socket
import requests

# host url google.com 
host = 'google.com'
port = 80
# port = 443
# cliet socket AF_INET, SOCK_STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client connect to host and port
client.connect((host, port))
# client send request tcp
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())
# client send request udp
# conv str to bytes

# client receive data
response = client.recv(4096)
# print response
print(response.decode())
# close client
client.close()
