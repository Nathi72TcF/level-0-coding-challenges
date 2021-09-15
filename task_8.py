time = float(input("Input time in numbers: "))

time = time % (24 * 3600)
hour = time // 60
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("h:m:s-> %02d:%02d:%02d" % (hour, minutes, seconds))