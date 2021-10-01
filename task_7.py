def convert_to_celsius(y):
    c = (y - 32) * 5/9
    return c


def convert_to_fahrenheit(y):
    f = (9/5 * y) + 32
    return f

x = "F"

if x == "F":
    convert_to_fahrenheit(20)

if x == "C":
    convert_to_celsius(20)
