


import math

height = 4
slant_height = 5
rate = 10

radius = math.sqrt(slant_height**2 - height**2)

base_area = math.pi * radius * radius
cost = base_area * rate

print("Radius =", radius)
print("Cost =", cost)
