import socket

HOST = '127.0.0.1'
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind((HOST, PORT))

server_socket.listen()
client_socket, addr = server_socket.accept()

print('Connected by: ', addr)

while True:
    data = client_socket.recv(1024)

    if not data:
        break

    print('Received from: ', addr, ', data: ', data.decode())
    ans = "(127.0001, 36.0008)"
    reply = ans.encode()
    client_socket.sendall(reply)

client_socket.close()
server_socket.close()