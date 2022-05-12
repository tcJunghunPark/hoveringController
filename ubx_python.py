from serial import Serial
from pyubx2 import UBXReader
import csv

#Create UBXReader object
stream = Serial('/dev/ttyACM0', 115200, timeout=1)
ubr = UBXReader(stream,validate=0)

#Read from incoming signals, sort out GNGGA msg that contain timestamp, lat, lng, and alt
while True:
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

        #write to csv file each time position data is parsed
        f = open("position_data.csv","a")

        writer = csv.writer(f)

        writer.writerow(log)

