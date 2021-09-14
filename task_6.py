a = int(input())
b = int(input())
c = int(input())

numbers = []

def maximum_number():
    numbers.append(a)
    numbers.append(b)
    numbers.append(c)
    print(max(numbers))

maximum_number()