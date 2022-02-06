
#  a*x*x + b*x + c
#https://math-prosto.ru/?page=pages/quadratic_equations/discriminant_of_quadratic_equation.php
import math

a = 2
b = 5
c = -7

# a = 16
# b = -8
# c = 1

# a = 9
# b = -6
# c = 2

d = b*b-4*a*c
print("D : " + d.__str__())

if (d <0):
    print("D < 0, немає дійсних коренів")
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("X1 : " + x1.__str__())
    print("X2 : " + x2.__str__())
