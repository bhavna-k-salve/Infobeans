



k =0
for i in range(5,-1,-1):
  for j in range(1,6):
    if j>i:
      print(k, end=" ")
    else:
      print(" ", end=" ")
  k += 1      
  print()  