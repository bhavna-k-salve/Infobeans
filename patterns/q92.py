
for i in range(1,6):
  if i<6:
    for k in range(1,6-i):
      print(" ",end="")
  for j in range(1,i+1):
    if ((i==3 or i==4) and j==2) or (i==4 and j==3):
      print("_",end=" ")
    else:  
      print("x",end=" ")
     
  print()   