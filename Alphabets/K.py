

for i in range(1,12):
  for j in range(1,7):
    if j==1 or (i<6 and i+j==7) or(i>6 and i-j==5):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()      