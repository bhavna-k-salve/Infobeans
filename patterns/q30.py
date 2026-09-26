


for i in range(6,0,-1):
  k=1
  for j in range(1,7):
    if j>i:
      if (i==3 and  j==5) or (i==2 and (j==5 or j==4)):
        print("_",end=" ")
        k+=1
      else:  
        print(chr(64+k), end=" ")
        k+=1
    else:
      print(" ", end=" ")  
  print()  