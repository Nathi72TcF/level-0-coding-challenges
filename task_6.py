def maximum_number(a, b, c):
    if (a >= b) and (a >= c):
        largest_number = a
    elif (b >= a) and (b >= c):
        largest_number = b
    else:
        largest_number = c

        print(largest_number)

maximum_number(3, 4, 5)
