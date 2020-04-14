import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
serversocket.bind((socket.gethostname(),port))
serversocket.listen(1)
while True:
    (clientsocket, address) = serversocket.accept()
    print(f"Połączenie z {address} zostało uzyskane")
    clientsocket.send(bytes("Rozpoczynanie transmisji danych", "utf-8"))
