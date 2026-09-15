


length = 30
width = 20
path1 = 3
path2 = 4

garden_area = length * width
path_area = (length * path1) + (width * path2) - (path1 * path2)

usable_area = garden_area - path_area

print("Usable area =", usable_area)