


for i in range(1,6):
  k=1
  for j in range(1,10):
    if i>j or j >= 11-i :
      print(" ",end="")
    elif i>1 and i<5 and (i==2 and (j!=2 and j!=8)) or (i==3 and (j!=3 and j!=7)) or (i==4 and (j!=4 and j!=6)):
      print("+",end="")  
      k+=1
    else:  
      print(k,end="")
      k+=1
  print()  
  