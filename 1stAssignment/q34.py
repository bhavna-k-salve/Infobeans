


base1 = 128
base2 = 92
height = 40
walkway = 4

trapezoid_area = (base1 + base2) * height / 2
walkway_area = walkway * height

remaining_area = trapezoid_area - walkway_area

print("Area after walkway =", remaining_area)