#Jarod Pierre Murton
#variable improvement exercise
#12-09-14

import math

radius = float(input("please enter the radius of the circle: "))

circumference = 2* math.pi * radius
circumference = round(circumference,2)

area = math.pi * radius**2
area = round(area,2)

print("The circumference of this circle is {0}.".format(circumference))
print("The area of this circle is {0}.".format(area))