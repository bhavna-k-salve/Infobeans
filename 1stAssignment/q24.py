

brick_long = 25
brick_wide = 10
brick_thick = 7.5

wall_long = 20
wall_high = 2 
wall_thick = 0.75


wall_volume = wall_long * wall_high * wall_thick
brick_volume = (brick_long/10) * (brick_wide/10) * (brick_thick/10)

number_of_bricks = wall_volume / brick_volume
cost = number_of_bricks / 1000 * 900

print("Number of bricks:", int(number_of_bricks))
print("Cost: ", cost)