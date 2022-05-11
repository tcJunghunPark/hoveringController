import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def right_button():
    client_socket.sendall('(1, 0)'.encode())
    coordinate = client_socket.recv(1024)
    print("(1,0)")
    print("received coordinate: ", repr(coordinate.decode()))
def left_button():
    client_socket.sendall('(-1, 0)'.encode())
    coordinate = client_socket.recv(1024)
    print("(-1,0)")
    print("received coordinate: ", repr(coordinate.decode()))
def up_button():
    client_socket.sendall('(0, 1)'.encode())
    coordinate = client_socket.recv(1024)
    print("(0,1)")
    print("received coordinate: ", repr(coordinate.decode()))
def down_button():
    client_socket.sendall('(0, -1)'.encode())
    coordinate = client_socket.recv(1024)
    print("(0,-1)")
    print("received coordinate: ", repr(coordinate.decode()))


#Main Function
HOST = input("Server Address: ")
PORT = int(input("Server PORT: "))
sleep_time = int(input("Signal Change Interval(in minutes): ")) * 60

funcs = [right_button, left_button, up_button, down_button]
try:
    client_socket.connect((HOST,PORT))
except socket.error:
    print("Socket Connection ERROR")
while True:
    try:
        time.sleep(5 * 60) # initial sleep time until signal stablized
        time.sleep(sleep_time)

        for f in funcs:
            f() # function call and sleep as input interval
            time.sleep(sleep_time)

    except KeyboardInterrupt as e:
        client_socket.close()
        break
    
    


    

    