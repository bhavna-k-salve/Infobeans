

for i in range(1,11):
  for j in range(1,11):
    if (i==j or (i+j)==11) and (i<6 or j<6):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print() 