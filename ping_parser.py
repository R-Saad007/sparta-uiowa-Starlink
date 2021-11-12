import datetime

# List to store the entire data elements for each ping recorded
data_list = []
def file_parser():
    # File Read
    f = open("test.txt", "r")
    for data in f:
        data = data.strip("\n")
        if data == '===========':
            data = f.readline()
            data = data.strip("\n")
            temp = data.split(' ')
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
    return data_list