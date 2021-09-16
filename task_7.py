# celsius = (c - 32) * 5/9       Formula
# fahrenheit = (9/5 * x) + 32        Formula

x = "F"      # F is selected
y = 20

def convert_to_celsius():
    c = (y - 32) * 5/9
    return c


def convert_to_fahrenheit():
    f = (9/5 * y) + 32
    return f


if x == "F":
    convert_to_fahrenheit()

if x == "C":
    convert_to_celsius()
