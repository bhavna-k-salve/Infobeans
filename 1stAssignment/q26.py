
path_long = 120
path_breadth = 2.4

brick_long = 24
brick_wide = 15

path_area = path_long * path_breadth
brick_area = (brick_long/100) * (brick_wide/100)
number = path_area / brick_area

print("Number of bricks:", int(number))