import math

def convert_time(time):
    hour = int(math.floor(time / 60))
    minutes = time % 60
    
    if hour == 1:
        print("%d hour %d minutes" % (hour, minutes))
    else:
        print("%d hours %d minutes" % (hour, minutes))

convert_time(61)