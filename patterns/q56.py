



for i in range(1,6):
  for j in range(1,i+1):
    if (i==3 or i==4) and (j==2 or j==3) and i!=j:
      print('_',end=" ")
    else:
      print(chr(64+j),end=" ")  
  print()  