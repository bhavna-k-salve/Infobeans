


for i in range(1,6):
  for j in range(1,6):
    if (i>1 and j>2 ) or (i>4 and j>1):
      print(" ",end="")
    else:
      print(chr(64+j),end="")  
  print()   