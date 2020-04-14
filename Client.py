import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((socket.gethostname(), 1234))

msg = clientsocket.recv(1024)
print(msg.decode("utf-8"))