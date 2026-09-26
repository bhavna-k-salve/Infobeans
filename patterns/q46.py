

for i in range(1,8):
  for j in range(1,5):
    if j==1:
      print("1",end=" ")
    elif (i<5 and i==j):
      print(i,end=" ")
    elif (i>4 ) and i+j==8:
      print(j,end=" ")
    else:
      print(" ",end=" ")
  print()        