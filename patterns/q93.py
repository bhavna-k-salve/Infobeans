



for i in range(1,6):
  if i<6:
    for k in range(1,6-i):
      print(" ",end="")
  for j in range(1,i*2):
    if (i>1 and i<5) and (j>1 and j<i*2-1):
      print("*",end="")
    else:  
      print("1",end="")
     
  print()   