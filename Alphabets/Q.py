


for i in range(1,11):
  for j in range(1,11):
    if (i==1 and (j>4 and j<7) ) or (i==10 and (j>3 and j<8)) or (j==1 and (i>3 and i<8)) or (j==10 and (i>4 and i<7)) or (i==2 and (j==3 or j==8)) or (i==3 and (j==2 or j==9)) or (i==8 and (j==2 or j==9)) or (i==9 and (j==3 or j==8)) or (i>7 and i==j) :
      print("*",end="")
    else:
      print(" ",end=" ")
  print()      