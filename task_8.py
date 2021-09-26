import math

def convert_time(time):
    hour = int(math.floor(time / 60))
    minutes = time % 60
    
    if hour == 1:
        print("%02d hour %02d minutes" % (hour, minutes))
    else:
        print("%02d hours %02d minutes" % (hour, minutes))

convert_time(133)