


k =1
for i in range(6,0,-1):
  for j in range(6,0,-1):
    if i>j:
      print(k,end="")
    else:
      print(" ",end="")  
  k += 1    
  print()    