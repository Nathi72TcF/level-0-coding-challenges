def area_of_a_triangle(a, b, c):
    d = (a + b + c) / 2   

    area = (d*(d-a)*(d-b)*(d-c)) ** 0.5         #Area of trianle formula
    print('The area of the triangle is', area)

area_of_a_triangle(3, 4, 5)