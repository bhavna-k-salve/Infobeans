

for i in range(6,-1,-1):
  k=1
  for j in range(1,6):
    if i < 7-j:
      print(" ",end="")
    else:  
      print(chr(64+k),end=" ") 
      k += 1
  print()  