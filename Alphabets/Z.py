


for i in range(1,11):
  for j in range(1,11):
    if i==1 or i==10 or (i+j)==11:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()      