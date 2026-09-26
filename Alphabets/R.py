

for i in range(1,12):
  for j in range(1,7):
    if j==1 or (i>6 and i-j==5) or (i==1 and j<5) or (j==6 and (i<5 and i>2)) or (i==6 and j<5 ) or (j==5 and (i==5 or i==2)):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print() 