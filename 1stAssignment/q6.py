import math

side1 = 10
side2 = 9
perimeter = 36
semiPerimeter = 36/2
side3 = perimeter - (side1 + side2)
area = semiPerimeter * (semiPerimeter- side1) * (semiPerimeter - side2) * (semiPerimeter - side3)



print(math.sqrt(area))