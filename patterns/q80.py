



for i in range(1,6):
  k=1
  for j in range(1,6):
    if i>j:
      print(" ",end=" ")
    elif (i==2 and (j==3 or j==4)) or (i==3 and j==4) :
      print("_",end=" ")  
      k+=1
    else:
      print(k,end=" ")
      k+=1
  print()  