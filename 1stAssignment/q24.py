

brickLong = 25
brickwide = 10
brickthick = 7.5

walllong = 20
wallhigh = 2 
wallthick = 0.75


wallVolume = walllong * wallhigh * wallthick
brickVolume = (brickLong/10) * (brickwide/10) * (brickthick/10)

number_of_bricks = wallVolume / brickVolume
cost = number_of_bricks / 1000 * 900

print("Number of bricks:", int(number_of_bricks))
print("Cost: ", cost)