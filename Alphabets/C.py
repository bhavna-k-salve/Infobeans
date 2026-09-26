


for i in range(1,11):
  for j in range(1,9):
    if (j==1 and (i<9 and i>2)) or (i==1 and (j<9 and j>2))  or (i== 10 and j>2) or (i==2 and j==2) or (i==9 and j==2):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()      
      