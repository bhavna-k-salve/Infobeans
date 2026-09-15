
pathLong = 120
pathBreadth = 2.4

brickLong = 24
brickWide = 15

pathArea = pathLong * pathBreadth
brickArea = (brickLong/100) * (brickWide/100)
number = pathArea / brickArea

print("Number of bricks:", int(number))