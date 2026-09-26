
for i in range(5,-1,-1):
  for j in range(1,6):
    if i < 6-j:
      print(" ",end="")
    else:  
      print("*",end=" ")
  print()  