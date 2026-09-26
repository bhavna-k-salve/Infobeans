


for i in range(1,8):
  for j in range(1,15):
    if i==j or j+i==14:
      print("*",end="")
    else:
      print(" ",end="")
  print() 