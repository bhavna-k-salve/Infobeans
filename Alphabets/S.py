

for i in range(1,10):
  for j in range(1,8):
    if (i==1 and j>1) or (i==9 and j<7) or (j==1 and i<5 and i>1) or (j==7 and i>5 and i<9) or (i==5 and j>1 and j<7) :
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()      