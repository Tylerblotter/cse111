
# def compute_data(a, b, c, d):
#     return (a/b) * (a / (c**2 + d**2))

# print(compute_data(5, 4, 3, 2))
# print(compute_data(9, 1, 4, 6))



# a = float(input('What is your A number: '))
# b = float(input('What is your B number: '))
# c = float(input('What is your C number: '))
# d = float(input('What is your D number: '))

# x = (a/b) * (a / (c**2 + d**2))

# print(f'{x:.03f}')

# from math import sqrt

# def quadratic_formula(a, b, c):
#     return (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)

# print(quadratic_formula(22, 66, 9))


import math

def compute_area(r):
    return math.pi * r * r 

radius = float(input('Please enter a radius: '))

print(f'The area is: {compute_area(radius)}')