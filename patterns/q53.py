

for i in range(6,0,-1):
  for j in range(1,7):
    if j>i:
      if (i==3 and  j==5) or (i==2 and (j==5 or j==4)):
        print("*",end=" ")
      else:  
        print(1, end=" ")
    else:
      print(" ", end=" ")  
  print()  