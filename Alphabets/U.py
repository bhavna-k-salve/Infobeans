

for i in range(1,7):
  for j in range(1,6):
    if (j==1 or j==5 ) and i<5 or  i+j==9:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print() 