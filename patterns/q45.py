

for i in range(1,6):
  k=1
  for j in range(1,10):
    if i>j or j >= 11-i :
      print(" ",end="")
    else:  
      print(k,end="")
      k+=1
  print()  
  