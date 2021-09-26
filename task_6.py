def maximum_number(a, b, c):
    if (a >= b) and (a >= c):
        largest_number = a
    elif (b >= a) and (b >= c):
        largest_number = b
    elif (c >= a) and (c >= b):
            largest_number = c
            
            return largest_number

maximum_number(3, 4, 5)
