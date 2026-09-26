

for i in range(1,13):
  for j in range(1,12):
    if j==1 or j==11 or (i<=6 and i==j) or (i<6 and j+i==12) :
      print("*",end=" ")
    else:
      print(" ",end=" ") 
  print()       