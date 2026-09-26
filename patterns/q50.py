



for i in range(6,0,-1):
  k=1
  for j in range(6,0,-1):
    if i>j:
      print(k,end="")
      k+=1
    else:
      print(" ",end="")  
  print()    