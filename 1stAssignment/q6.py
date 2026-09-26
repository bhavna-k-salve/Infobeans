import math

side1 = 10
side2 = 9
perimeter = 36
semi_perimeter = 36/2
side3 = perimeter - (side1 + side2)
area = semi_perimeter * (semi_perimeter- side1) * (semi_perimeter - side2) * (semi_perimeter - side3)



print(math.sqrt(area))