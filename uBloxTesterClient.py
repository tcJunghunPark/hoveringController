from serial import Serial
from pyubx2 import UBXReader
import csv, socket, time


stream = Serial('/dev/ttyACM0', 115200, timeout=1)
ubr = UBXReader(stream,validate=0)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

f = open("position_data.csv","a")
writer = csv.writer(f)

flag = [-1,-1,-1,-1]

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

time.sleep(5 * 60) # initial sleep time until signal stablized
counter = 0
func_counter = 0

while True:
    try:
        if counter <= sleep_time:
            (raw_data,parsed_data) = ubr.read()

            print("parsed data: ", parsed_data)
            print("type: ", type(parsed_data))

            if parsed_data!=None and parsed_data.identity == "GNGGA":
                str_data = str(parsed_data)[6:-2]
                list_data = str_data.split(',')
                time = list_data[1][6:]
                lat = list_data[2][5:]
                lon = list_data[4][5:]
                alt = list_data[9][5:]

                log = [time,lat,lon,alt]
                writer.writerow(log) # wirte log to csv file
                counter += 1
                
        elif func_counter < len(funcs):
            writer.writerow(flag)
            funcs[func_counter]()
            func_counter += 1
            counter = 0
        else:
            print("system end!")
            break

    except KeyboardInterrupt as e:
        client_socket.close()
        break
    except Exception as e:
        print(e)
        break

    