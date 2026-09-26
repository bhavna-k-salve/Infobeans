
for i in range(1,6):
  k=1
  for j in range(1,6):
    if i>j:
      print(" ",end=" ")
    else:
      print(chr(64+k),end=" ")
      k+=1
  print()  