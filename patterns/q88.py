
for i in range(1,7):
  if i<7:
    for _ in range(1,7-i):
      print(" ",end="")
  for j in range(1,i+1):
    print(chr(64+j),end=" ")
     
  print()     