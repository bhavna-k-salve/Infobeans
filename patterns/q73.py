

for i in range(1,6):
  for j in range(1,i+1):
    if (j>2 and i>1 and i<5):
      print(" ",end="")
    elif(i%2==0 and j%2==0) and j!=1:
      print(0,end="")
    else:  
      print(1,end="")
  print()  