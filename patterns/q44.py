

for i in range(1,6):
  if i<6:
    for k in range(1,6-i):
      print(" ",end="")
  for j in range(1,i*2):
    if i==j:
      print("#",end="")
    else:  
      print("*",end="")
     
  print()   