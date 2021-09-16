def convert_time(time):
    time = time % (24 * 3600)
    hour = time // 60
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print("%02d hours, %02d minutes, %02d seconds" % (hour, minutes, seconds))

convert_time(133)
