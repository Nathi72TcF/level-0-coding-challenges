# import math

def convert_time(time):
    hour = int(time / 60)
    minutes = time % 60
    
    if hour == 1 and minutes == 1:
        print("%d hour %d minute" % (hour, minutes))
    elif hour == 1:
        print("%d hour %d minutes" % (hour, minutes))
    elif minutes == 1:
        print("%d hours %d minute" % (hour, minutes))
    else:
        print("%d hours %d minutes" % (hour, minutes))

convert_time(133)