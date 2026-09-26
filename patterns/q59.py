


for i in range(5,-1,-1):
  k = 1
  for j in range(1,6):
    if j>i:
      print(chr(64+k), end=" ")
      k += 1
    else:
      print(" ", end=" ")  
  print()  