



for i in range(1,9):
  for j in range(1,19):
    if (i+j==11) or (j-i==9) or (j>5 and i==5 )and (j<15 and i==5) :
      print("*",end=" ")
    else:
      print(" ",end=" ") 
  print()      