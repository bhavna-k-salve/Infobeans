

for i in range(1,12):
  for j in range(1,8):
    if (i==1 and j<6) or (i==11 and j<6) or j==1 or (j==7 and (i>2 and i<10)) or (j==6 and (i==2 or i==10)):
      print("*",end=" ")
    else:
      print(" ",end=" ")  
  print()    