import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def right_button():
    client_socket.sendall('(1, 0)'.encode())
    coordinate = client_socket.recv(1024)
    print("received coordinate: ", repr(coordinate.decode()))
def left_button():
    client_socket.sendall('(-1, 0)'.encode())
    coordinate = client_socket.recv(1024)
    print("received coordinate: ", repr(coordinate.decode()))
def up_button():
    client_socket.sendall('(0, 1)'.encode())
    coordinate = client_socket.recv(1024)
    print("received coordinate: ", repr(coordinate.decode()))
def down_button():
    client_socket.sendall('(0, -1)'.encode())
    coordinate = client_socket.recv(1024)
    print("received coordinate: ", repr(coordinate.decode()))


#Main Function
HOST = input("Server Address: ")
PORT = int(input("Server PORT: "))

try:
    client_socket.connect((HOST,PORT))
except socket.error:
    print("Socket Connection ERROR")
while True:
    try:
        command = input("ENTER u d r l, ctrl + c to quit: ")
        command = command.lower()
    except KeyboardInterrupt as e:
        client_socket.close()
        break

    if command == "u":
        up_button()
        print("Send (0,1)")
        continue
    elif command == "d":
        down_button()
        print("Send (0,-1)")
        continue
    elif command == "r":
        right_button()
        print("Send (1,0)")
        continue
    elif command == "l":
        left_button()
        print("Send (-1,0)")
        continue
    else:
        print("Wrong input!")
        continue
    

    