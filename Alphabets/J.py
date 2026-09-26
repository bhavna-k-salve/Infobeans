

for i in range(1,10):
  for j in range(1,10):
    if i==1 or (j==5 and i<8 ) or (i==9 and j<4 and j>3) or (j==1 and i>5 and i<8) or (i==8 and (j==2 or j==4)):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()      