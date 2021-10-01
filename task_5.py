def area_of_a_triangle(a, b, c):
    d = (a + b + c) / 2   

    area = (d*(d-a)*(d-b)*(d-c)) ** 0.5
    return area

area_of_a_triangle(3, 4, 5)