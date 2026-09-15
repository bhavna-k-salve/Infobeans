

import math

volume = 1287
radius = 10

height = volume / (math.pi * radius * radius)

surface_area = 2 * math.pi * radius * (radius + height)

print("Height =", height)
print("Surface area =", surface_area)