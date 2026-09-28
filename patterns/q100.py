




for i in range(1,5):
  if i<5:
    for _ in range(1,5-i):
      print(" ",end="")
  for j in range(1,i*2):
    if i==j and i>1 or (j>1 and j<i*2-1):
      print("_",end="")
    else:
      print("*",end="")
  print() 
  

for i in range(1,5): 
  for j in range(1,7):
    if i>=j or i+j>7:
      print(" ",end="")
    elif i+1<j and i+j<7 :
      print("_",end="")  
    else:  
      print("*",end="")   
  print()   