from re import sub
import skyfield
import os
import datetime
from skyfield.api import load, wgs84
from skyfield.api import EarthSatellite
from math import cos, asin, sqrt, pi
import time


# To measure the execution speed of the program, we initialize our start time
start_time = time.time()


# # For Version Check
# if skyfield.VERSION < (1, 24):
#     print("Old Version")


# Setting path to read all TLE data files
path = r"C:\Users\HP\Documents\Neo\Research\Starlink-UIOWA\Skyfield\Satellite_Data"
os.chdir(path)


# Function to return the necessary first 2 lines for each TLE data file to create satellite object
def tle_data(file_name):
    with open(file_name, 'r') as f:
        f_line = f.readline()
        s_line = f.readline()
    return f_line, s_line


# Making use of Haversine Formula to get the distance between 2 points using their longitude and latitude values
def Haversine_distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * \
        cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))  # 2*R*asin...


# Function to convert longitude and latitude values to decimal form
def parser(data):
    parts = data.split()
    parts[0] = float(parts[0][:-3])
    parts[1] = (float(parts[1][:-1]))/60.0
    parts[2] = (float(parts[2][:-1]))/(60.0*60.0)
    if parts[0] < 0.0:
        parts[0] *= -1
        result = parts[0] + parts[1] + parts[2]
        result *= -1
        return result
    elif parts[0] >= 0.0:
        result = parts[0] + parts[1] + parts[2]
        return result


# Code below only loads the data for one satellite and stores it in a dictionary
'''
sat_file = 'Satellite_Data/sat44238.txt'
satellites = load.tle(sat_file)
print('Loaded', len(satellites), 'satellite/s')
'''


# List to store the entire data elements for each ping recorded for one week
data_list = []
# This function extracts and parses data from the ping data file
def file_parser():
    # File Read
    f = open(r"C:\Users\HP\Documents\Neo\Research\Starlink-UIOWA\Skyfield\week1_ping_data.txt", "r")
    for data in f:
        data = data.strip("\n")
        if data == '===========':
            data = f.readline()
            data = data.strip("\n")
            temp = data.split(' ')
            if temp[4] == "PM" or temp[4] == "AM":
                day = temp[2]
                month = datetime.datetime.strptime(temp[1], "%b").month
                year = temp[6]
                time = temp[3]
                time = time.split(':')
                hours = time[0]
                minutes = time[1]
                seconds = time[2]
                temp = (year, month, day, hours, minutes, seconds)
                data_list.append(temp)
            else:
                day = temp[3]
                month = datetime.datetime.strptime(temp[1], "%b").month
                year = temp[7]
                time = temp[4]
                time = time.split(':')
                hours = time[0]
                minutes = time[1]
                seconds = time[2]
                temp = (year, month, day, hours, minutes, seconds)
                data_list.append(temp)
            for x in range(5):
                data = f.readline()
            data = data.strip("\n")
            if data != '1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms':
                del(data_list[-1])
    f.close()
    print("Ping data parsed successfully!\n")
    return data_list


# Initializing a counter variable to count the number of packet losses, due to absense of satellites (genuine packet losses)
genuine_packet_loss = 0
# Initializing a boolean variable to keep track of genuine packet losses
check = True
# Changing antenna location according to a x meter shift in all 4 directions (N,S,E,W)
antenna_shift_distance  = 500000
# Radius of the earth
radius_earth = 6378.137
# 1 meter in degree
m = (1 / ((2 * pi / 360) * radius_earth)) / 1000
North = 40.43742 + (antenna_shift_distance * m)
South = 40.43742 - (antenna_shift_distance * m)
East = -86.90778 + (antenna_shift_distance * m) / cos(-86.90778 * (pi / 180))
West = -86.90778 - (antenna_shift_distance * m) / cos(-86.90778 * (pi / 180))
# Checking whether a satellite is within a distance x from the antenna where distx is the variable to be changed
distx = input("Enter the distance for satellite tracking: ")
distance_from_antenna = int(distx)
# Calling the parser function from the ping_parser file
data_list = file_parser()
for x in range(len(data_list)):
    print("{:.4f}".format((x/len(data_list))*100),"% completed")
    #Storing value of the data contained in the data_list for each iteration
    temp_data = data_list[x]
    # Setting timescale element
    # Here we can set the timescale value of our choice
    ts = load.timescale()
    t_data = ts.utc(int(temp_data[0]), month=int(temp_data[1]), day=int(temp_data[2]), hour=int(temp_data[3]), minute=int(temp_data[4]), second=int(temp_data[5]))
    # List to store all satellites's data (satellite name, latitude, longitude, Height, Epoch)
    satellite_data_list = []
    # List to store the names of certain satellites after the distance calculations have been performed using the Haversine formula
    satellite_name_list = []
    # List to store the particular distance values of each satellite from the antenna
    distance_list = []
    # Retrieving data for all satellites
    # Input for the distance from the antenna for which satellites are to be found
    '''
    This is part of the previous testing code
    x = float(input("Enter the distance from the antenna for which satellites are to be found: "))
    '''
    for file in os.listdir():
        if file.endswith(".txt"):
            satellite_name = str(os.path.splitext(os.path.basename(file))[0])
            file_path = f"{path}\{file}"
            line1, line2 = tle_data(file_path)      
            # 2 line TLE data required to instantiate a satellite object
            sat_data = EarthSatellite(line1, line2)
            geocentric_position = sat_data.at(t_data)
            # subpoint converts the geocentric positioning to the latitude and longitude system
            subpoint = wgs84.subpoint(geocentric_position)
            # adding the satellite data to the list
            satellite_data_list.append((satellite_name,str(subpoint.latitude), str(subpoint.longitude), subpoint.elevation.km, sat_data.epoch.utc_jpl()))
            # Latitude and Longitude values of the satellite
            latitude_val = str(subpoint.latitude)
            longitude_val = str(subpoint.longitude)
            # The converted decimal values for the latitude and longitude of the satellite
            decimal_latitude_val = parser(latitude_val)
            decimal_longitude_val = parser(longitude_val)
            # Distance of the satellite from the antenna using Haversine formula
            distance_data = Haversine_distance(40.43742, -86.90778, decimal_latitude_val, decimal_longitude_val)
            # This means that a satellite exists, hence packet loss might raise concerns about Starlink connectivity issues provided data collection is not corrupted
            if distance_data <= distance_from_antenna:
                check = False
                satellite_name_list.append(satellite_name)
                distance_list.append(distance_data)
        else:
            print("File does not exist!")
    if check:
        # This means that a satellite does not exist, hence packet loss is due to absense of connectivity node
        genuine_packet_loss += 1
    # Reverting back changed value
    check = True


print(f"Number of satellites at a distance of {distance_from_antenna}km from the antenna:", len(satellite_name_list))
print("Number of genuine packet losses:", genuine_packet_loss)
accuracy = (genuine_packet_loss/(genuine_packet_loss + len(satellite_name_list)))*100
print("Percentage disconnections/packet losses related to absense of satellites:",accuracy)
print("Execution Time: " + "{:.4f}".format((time.time() - start_time)) + "seconds")


# The code below belongs for previous testing purposes
# print(f"Number of satellites at a distance of {x}km from the antenna:", len(satellite_name_list))
# for x in range(len(satellite_name_list)):
#     print("Satellite:",satellite_name_list[x])
#     print("Distance from antenna:",distance_list[x],"km")


# 500 km North Output:
'''
Number of satellites at a distance of 300km from the antenna: 2
Number of genuine packet losses: 121
Percentage disconnections/packet losses related to absense of satellites: 98.3739837398374
'''
# 500 km South Output:
'''
Number of satellites at a distance of 300km from the antenna: 1
Number of genuine packet losses: 262
Percentage disconnections/packet losses related to absense of satellites: 99.61977186311786
'''
# 500 km East Output:
'''
Number of satellites at a distance of 300km from the antenna: 2
Number of genuine packet losses: 313
Percentage disconnections/packet losses related to absense of satellites: 99.36507936507937
'''
# 500 km West Output:
'''
Number of satellites at a distance of 300km from the antenna: 3
Number of genuine packet losses: 512
Percentage disconnections/packet losses related to absense of satellites: 99.41747572815534
'''
# Normal Output:
'''
Number of satellites at a distance of 300km from the antenna: 2
Number of genuine packet losses: 319
Percentage disconnections/packet losses related to absense of satellites: 99.37694704049844
'''
# The time for which satellites aren't available in a 24 hour format
'''
319 packet losses in 1 week so 45 packet losses in 1 day.
Each packet loss/disconnection time period averages on 25 seconds/loss, hence total time for which satellites are not available in a 24 hour format = 1125 seconds or 18.75 minutes
'''


# Assumptions:
# 1) Not taking into account the newly launched satellites (September onwards)
# 2) Assuming the satellites follow a similar trajectory
# 3) Assuming that the antenna is connected to a satellite that is closer i.e. (Sat A) at 100 km and (Sat B) at 200 km, so Sat A is connected with.